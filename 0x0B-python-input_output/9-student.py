#!/usr/bin/python3

"""
module that houses a class

"""


class Student:
    """
    Student class that defines a class
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiates a Student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        public instance method that retrieves and
        returns a dictionary representation of a
        Student instance
        """

        return self.__dict__
