#!/usr/bin/python3
""" Module of a square class"""


class Square:
    """Blueprint of object"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of an object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size of the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position the object"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the object"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square as # to stdout"""
        if self.__size == 0:
            print()
            return

        else:
            for k in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for x in range(0, self.__size):
                    print("#", end="")
                print()
