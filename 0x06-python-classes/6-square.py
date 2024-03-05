#!/usr/bin/python3

""" a class called Square that defines a square """


class Square:
    """ a class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ instantiates every object of this square class """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ private instance attribute getter (__size)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ private instance attribute setter (__size) """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ private instance getter attribute (__position) """
        return self.__position

    @position.setter
    def position(self, value):
        """ private instance setter attribute (__position) """
        err = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(err)
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError(err)
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError(err)
        self.__position = value

    def area(self):
        """ computes and returns the area of the square object """
        return self.size ** 2

    def my_print(self):
        square = '#'
        spaces = ' '

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("{}".format(spaces * self.position[0]), end='')
                for i in range(self.size):
                    print("{}".format(square), end="")
                print()
