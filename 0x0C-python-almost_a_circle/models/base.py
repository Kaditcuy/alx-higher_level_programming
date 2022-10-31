#!/usr/bin/python3
"""Module containing Base class"""
import json


class Base():
    """Base class, blueprint for all Base objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes object of the Base class

        Args:
            self: refers to current instance of the class
            id: set to None as default
        """
        if id != None:
            self.id = id
        elif id == None:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation
        of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the
        json string representation of list_objs
        to a file.

        Args:
            cls: refers to the class
            list_objs: list of objects who inherits Base
        """
        filename = cls.__name__ + ".json"
        list_of_dicts = []
        with open(filename, "w") as a_file:
            if list_objs is None:
                a_file.write("[]")
            else:
                for item in list_objs:
                    list_of_dicts.append(cls.to_dictionary(item))
                jsonstr = cls.to_json_string(list_of_dicts)
                a_file.write(jsonstr)

    @staticmethod
    def from_json_string(json_string):
        """Decodes a json srring format"""
        if json_string is None:
            return []
        return json.loads(json_string)
