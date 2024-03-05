#!/usr/bin/python3

"""
module that houses a function that
returns the json representation of python objects
if serializable
"""


def to_json_string(my_obj):
    """
    to_json_string - function to return json representation
    of a python object if serializable

    Args:
       my_obj: python object to be converted to json string

    Return:
       json string representation of the python object
    """

    import json

    return json.dumps(my_obj)
