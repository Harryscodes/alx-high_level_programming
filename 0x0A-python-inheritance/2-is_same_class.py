#!/usr/bin/python3

""" module that houses a function that verifies if
an object is an instance of an exact class """


def is_same_class(obj, a_class):
    """
    function to verify if an object is
    an instance of an exact class

    Args:
       obj: the object to be checked

       a_class:the class in which the object
       is checked against

    Returns:
       either True or False depending
       on if obj is an instance of a_class of not
    """

    if type(obj) == a_class:
        return True
    else:
        return False
