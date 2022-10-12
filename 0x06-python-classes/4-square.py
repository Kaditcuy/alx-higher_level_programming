#!/usr/bin/python3
""" Module of Class Square"""


class Square:
    """Blueprint of a square objct"""

    def __init__(self, size=0):
        """Initialize a new square.
        
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
       """Gets the current size of the square."""
       return (self.__size)

    @size.setter
    def size(self, value):
        """sets the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
         """Return the current area of the square."""
         return (self.__size * self.__size)
