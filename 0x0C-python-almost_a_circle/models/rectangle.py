#!/usr/bin/python3
"""
``Rectangle``class
"""
from turtle import width
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width value
        Reurn: Private width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter forr width value
        """
        self.__width = width

    @property
    def height(self):
        """
        getter for height value
        Return: Private height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter forr width value
        """
        self.__height = height

    @property
    def x(self):
        """
        Getter for x value
        Return: Private x value
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter for x value
        """
        self.__x = x

    @property
    def y(self):
        """
        Getter for y value
        Return: Private y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter for y value
        """
        self.__y = y
