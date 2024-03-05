#!/usr/bin/python3

""" module that has MyInt class """


class MyInt(int):

    """ 
    MyInt class is a rebel class that
    inherents from python int class
    and negates the result of == and !=

    Args:
       int: python int class being inheritted from

    """
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
