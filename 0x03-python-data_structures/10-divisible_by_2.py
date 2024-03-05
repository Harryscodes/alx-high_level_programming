#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    returns a list with boolean value
    if element is even number or not
    """
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
