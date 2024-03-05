#!/usr/bin/python3

def no_c(my_string):
    """ function to remove c from passed string """
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] not in ('c', 'C'):
            new_str += my_string[i]
    return new_str
