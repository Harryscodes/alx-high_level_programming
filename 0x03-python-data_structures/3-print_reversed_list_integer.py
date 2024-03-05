#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ function to print list element in reverse """
    if not my_list:
        pass
    else:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
