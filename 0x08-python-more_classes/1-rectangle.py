#!/usr/bin/python3

"""module that houses a class Rectangle """


class Rectangle:
    """ a class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes all instances of this class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for the width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
