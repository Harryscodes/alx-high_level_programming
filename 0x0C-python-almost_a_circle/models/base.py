#!/usr/bin/python3

"""
module to house a class called Base
"""

import json
import os
import csv


class Base:
    """
    Base class for create methods and attributes
    other sub-class can inherit
    """

    __nb_objects = 0
    __true_nb_objects = 0
    __properties = {}

    def __init__(self, id=None) -> None:
        """
        __init__ - instance initialization of a base instance

        Args:
           self: reference to the instance being created
           id: optional parameter that cater to the supposed
           id of that instance

        Return:
           None is returned
        """
        key = str(Base.__true_nb_objects)
        baseclass = self.__class__.__base__.__name__
        if id is not None:
            if id < 0:
                raise ValueError('id can not be < 0')
            self.id = id
            Base.__true_nb_objects += 1
            Base.__properties[key] = self.__dict__
            Base.__properties[key]["class"] = self.__class__.__name__
            Base.__properties[key]['baseclass'] = baseclass
        else:
            Base.__nb_objects += 1
            Base.__true_nb_objects += 1
            self.id = self.__nb_objects
            Base.__properties[key] = self.__dict__
            Base.__properties[key]["class"] = self.__class__.__name__
            Base.__properties[key]['baseclass'] = baseclass

    @classmethod
    def resetclasspri_attr(cls):
        """ public class method to reset all class private attribute """
        cls.__nb_objects = 0
        cls.__true_nb_objects = 0
        cls.__properties.clear()

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - method to convert a list
        of dictionaries to json string representation

        Args:
           list_dictionaries: a list of dictionaries that is to
           be converted to json string representation

        Return:
             a string rep. of an empty list if list_dictionaries
             is not provided or empty
             Or a string representation ofthe provided list
             of dictionaries
        """
        if list_dictionaries:
            if len(list_dictionaries) == 0:
                return '[]'
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - method to save dictionaries of all
        class object  as to a file

        Args:
           cls: reference to the class itself
           list_object: list of all dictionary objects
           to be saved into the file

        Return:
           Nothing is to be returned therefore None is returned
        """
        if list_objs is None:
            list_objs = []

        if not isinstance(list_objs, list):
            raise TypeError("list_object must be a either list or None")

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as f:
            rp = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(rp)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - a static method
        that returns the list of the JSON
        string representation json_string:

        Args:
        json_string: is a string
        representing a list of dictionaries

        Returns:
        If json_string is None or empty,
        return an empty list Otherwise,
        return the list represented by
        json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - method that returns an instance with
        all attributes already set

        Args:
           cls: reference to the class
           **dictionary: dictionary element being unpacked

        Return:
           New instance of the provided dictionary
        """

        newInstance = cls(**dictionary)
        newInstance.update(**newInstance.to_dictionary())
        return newInstance

    @classmethod
    def load_from_file(cls):
        """
        load_from_files - method that reads from a file and
        then, returns a list of instances

        Args:
           cls: reference to the class

        Returns:
           an empty list if file doesnt exist or a
           list of instance
        """

        filename = cls.__name__ + '.json'

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            json_rep = f.read()
        obj = cls.from_json_string(json_rep)
        instance = [cls.create(**instance) for instance in obj]
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv - method to save serialized 
        python objects into a CSV file
        Args:
           cls: reference to class calling on this method
           list_objs: reference of list instance expected
           in this function

        Return: None
        """
        filename = cls.__name__ + '.csv'

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                writer.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ 
        load_from_file_csv - method to load serialized
        data from CSV file into a python program

        Args:
           cls: reference of the class calling
           load_from_file_csv method

        Return:
           a list of python objects representing data in
           the CSV file
        """

        filename = cls.__name__ + '.csv'
        instances = []

        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = Rectangle(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                elif cls.__name__ == "Square":
                    instance = Square(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                instances.append(instance)

        return instances
