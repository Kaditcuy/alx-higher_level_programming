#!/usr/bin/python3
"""Module of a Class Square"""


class Square:
    "Blueprint of a square object"""

    def __init__(self, size=0):
        """Initializes a square object"""
        self.size = size

    @property
    def size(self):
        """Gets the size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a diagrammatic rep of square"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end="")
                print()
