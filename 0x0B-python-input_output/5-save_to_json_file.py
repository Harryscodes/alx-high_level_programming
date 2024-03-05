#!/usr/bin/python3

"""
module that houses a function that saves
a python object as a json string into a json file
"""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function to save python
    object into a json file

    Args:
       my_obj: python object to be saved in json file
       filename: name of the json file in which the
       python object is to be saved

    Return:
       None is returned
    """
    import json

    json_rep = json.dumps(my_obj)
    with open(filename, 'w', encoding='UTF8') as f:
        f.write(json_rep)
