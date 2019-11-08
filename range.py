"""implement python2 range() without using range on whiteboard"""
# ie a list generator
"""start, stop step are integers can be positive or negative"""
import operator


def whiteboard_range(start, stop, step):
    if type(start) is not int:
        raise ValueError("Start must be integer")
    elif type(stop) is not int:
        raise ValueError("Stop must be integer")
    elif type(step) is not int:
        raise ValueError("Step must be integer")
    elif step == 0:  # we want this to be 0
                     # this is an easy way to express it
        raise ValueError("Step must not be 0")
    elif (step > 0) and (start > stop):
        raise ValueError("Step must not be 0")
    elif (step < 0) and (start < stop):
        raise ValueError("Step must not be 0")

    if step > 0:
        statement = operator.lt
    else:
        statement = operator.gt
    return_list = []

    while statement(start, stop):
        return_list.append(start)
        start += step

    return return_list
