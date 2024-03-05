#!/usr/bin/python3

"""
module that house a base class BaseGeometry
and other sub-classes
"""


class BaseGeometry:
    """
    base class
    """
    def area(self):
        """ public instance method for area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method to validate value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):

    """
    Rectangle class inheriting from BaseGeometry class

    Args:
       BaseGeometry: Base class being inheritted from
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
        super().__init__()
