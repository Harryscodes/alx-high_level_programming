#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # my_list: is the initial list
    # search: is the element to replace in the list
    # replace: is the new element

    new_list = [*my_list]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
