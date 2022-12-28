#!/usr/bin/python3
"""
Module of a Square Class
"""


class Square:
    """ Blueprint of a square"""

    def __init__(self, size):
        """Attributes to Initialize a new square object with.


        Args:
            size (int): The size of the new square.
        """
        self.__size = size
