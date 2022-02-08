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
    