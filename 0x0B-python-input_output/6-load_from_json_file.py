#!/usr/bin/python3

"""
module that houses a function that creates
a python object from a json file
"""


def load_from_json_file(filename):
    """
    load_from_json_file - function to load python
    object from a json file

    Args:
       my_obj: python object to be saved in json file
       filename: name of the json file in which the
       python object is to be loaded from

    Return:
       None is returned
    """
    import json

    with open(filename, 'r', encoding='UTF8') as f:
        json_rep = f.read()
        return json.loads(json_rep)
