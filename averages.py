"""
Write a class in python that has the following interface:
a = avgCalculate()
a.update(number)
a.getAvg() : return a number which is the average of all the numbers called by update.


The requirement is for this class to be O(1) in space and calculation

Also write 4 tests using python unitest
Usage of the class  may look like
a=avgCalculate()
a.update(1)
a.update(2)
print( a.getAvg())
and the output will be

1.5
"""

import unittest


class avgCalculate:

    def __init__(self):
        self.average = 0
        self.count = 0

    def update(self, number):
        weight = self.average * self.count
        self.count += 1
        self.average = (weight + number) / self.count

    def getAvg(self):
        return self.average


class AverageTester(unittest.TestCase):
    def test_easy(self):  # expecting 1.5
        a = avgCalculate()
        a.update(1)
        a.update(2)
        self.assertEqual(a.getAvg(), 1.5)

    def test_zero(self):  # expecting 0
        a = avgCalculate()
        for e in range(100):
            a.update(0)
        self.assertEqual(a.getAvg(), 0)

    def test_negative(self):  # expecting 0
        a = avgCalculate()
        for e in range(-100, 101):
            a.update(e)
        self.assertEqual(a.getAvg(), 0)

    def test_large(self):  # expecting 0
        a = avgCalculate()
        for e in range(-5000000, 5000001):
            a.update(e)
        self.assertEqual(a.getAvg(), 0)


if __name__ == '__main__':
    unittest.main()
