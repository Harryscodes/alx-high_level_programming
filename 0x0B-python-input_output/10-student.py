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

    def to_json(self, attrs=None):
        """
        public instance method that retrieves and
        returns a dictionary representation of a
        Student instance

        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """

        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
