#!/usr/bin/python3
"""Module containing Rectangle class
which is a sub class of parent Base class"""
from models.base import Base

class Rectangle(Base):
    """Base class, blueprint for all Base objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes object of the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.heigth = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for private
        instance variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for private
        instance variable width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """getter method for private
        instance variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for private
        instance variable height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self):
        """getter method for private
        instance variable x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for private imstance
        variable x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be a positive integer")
        self.__x = value

    @property
    def y(self):
        """getter method for private
        instance variable y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for private
        instance variable y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be a positive integer")
