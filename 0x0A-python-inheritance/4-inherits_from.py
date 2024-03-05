#!/usr/bin/python3

"""
module that houses a function that verifies if
an object is an instance of a class that is
inherented from other class or not
"""


def inherits_from(obj, a_class):
    """
    function to verify if an object is
    inheritted from a class

    Args:
       obj: the object to be checked

       a_class:the class in which the object
       is checked against

    Returns:
       either True or False depending
       on if obj is an instance of a_class of not
    """

    baseclasses = obj.__class__.__bases__

    for ob in baseclasses:
        if isinstance(obj, ob):
            return True
    return False
