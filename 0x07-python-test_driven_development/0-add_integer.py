#!/usr/bin/python3

""" module for function to add 2 numbers """


def add_integer(a, b=98):
    """ function to add 2 numbers
    Args:
        a: first number
        b: second number
    Returns:
        The sum of a and b

    Raises:
         TypeError if a or b is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
