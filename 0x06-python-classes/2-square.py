#!/usr/bin/python3
"""
Module of a Class Square
"""


class Square:
    """Blueprint of a square"""

    def __init__(self, size=0):
        """ Initializes a new square object with attributes

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
