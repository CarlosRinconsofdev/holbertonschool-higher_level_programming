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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        """
        getter for width value
        Reurn: Private width value
        """
        return self.width

    def set_width(self, width):
        """
        setter forr width value
        """
        self.__width = width

    def get_height(self):
        """
        getter for height value
        Return: Private height value
        """
        return self.height

    def set_height(self, height):
        """
        setter forr width value
        """
        self.__height = height

    def get_x(self):
        """
        Getter for x value
        Return: Private x value
        """
        return self.x

    def set_x(self, x):
        """
        setter for x value
        """
        self.__x = x

    def get_y(self):
        """
        Getter for y value
        Return: Private y value
        """
        return self.y

    def set_y(self, y):
        """
        setter for y value
        """
        self.__y = y
