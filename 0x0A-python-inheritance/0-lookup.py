#!/usr/bin/python3

""" module that houses function that return a list
of all attributes and methods associated with an object
"""


def lookup(obj):
    """
    returns list of all attributes
    and methods associated with a given object

    Args:
        obj: object whose properties is to be returned

    Return:
        a list of all properties of given object
    """

    return dir(obj)
