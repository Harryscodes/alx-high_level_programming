#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ returns a newly modified list """
    if idx < 0 or idx > len(my_list) - 1:
        return [my_list[i] for i in range(len(my_list))]
    new_list = [my_list[i] for i in range(len(my_list))]
    new_list[idx] = element
    return new_list
