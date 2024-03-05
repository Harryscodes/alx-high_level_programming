#!/usr/bin/python3

"""
module that holds a function that
returns the dictionary representation
of a python object
"""


def class_to_json(obj):
    """
    function to returns the dictionary
    discription of a python object,
    with simple structure

    Args:
      obj: python obj to be returned as a
      simple dictionary object for JSON serialization

    Returns:
      a dictionary representation of the python object

    """
    return obj.__dict__
