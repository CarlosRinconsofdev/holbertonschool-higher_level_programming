#!/usr/bin/python3
"""
``Rectangle``class
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.widht = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """
        Property for width value
        Return: Private width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter forr width value
        """
        self.__width = value
    
    @property
    def height(self):
        """
        Property for height value
        Return: Private height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter forr width value
        """
        self.__height = value

    @property
    def x(self):
        """
        Property for x value
        Return: Private x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x value
        """
        self.__x = value

    