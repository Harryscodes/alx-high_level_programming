#!/usr/bin/python3
""" a class called Square that defines a square """


class Square:
    """ a class that defines a square """

    def __init__(self, size=0):
        """ instantiates every object of this square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ computes and returns the area of the square object """
        return self.__size ** 2
