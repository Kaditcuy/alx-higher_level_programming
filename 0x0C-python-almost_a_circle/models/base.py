#!/usr/bin/python3
"""Module containing Base class"""

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