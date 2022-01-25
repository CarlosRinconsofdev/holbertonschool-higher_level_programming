#!/usr/bin/python3
""" Write a class that defines a rectangle """


class Rectangle:
    """Write a class  that defines a rectangle with
    privates attributes"""

    def __init__(self, width=0, height=0):
        """Initializes method data"
        Args:
            width (int): integer width
            height (int): integer height        
        """
        self.__height = height
        self.__width = width


    @property
    def height(self):
        """Private instance height of the rectangle"""
        return self.__height


    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    @property
    def width(self):
        """Private instance height of the rectangle"""
        return self.__width


    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
