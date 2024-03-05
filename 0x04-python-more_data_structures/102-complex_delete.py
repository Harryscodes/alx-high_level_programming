#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    new_dict = {k: v for k, v in a_dictionary.items()}
    for k, v in new_dict.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
