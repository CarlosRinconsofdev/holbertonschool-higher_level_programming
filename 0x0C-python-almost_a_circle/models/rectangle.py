#!/usr/bin/python3
"""
``Rectangle``class
Update the class adding the public method def display(self):
that prints in stdout the Rectangle instance with the character #
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

    def area(self):
        """
        Update the class
        Return: the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Update the class that prints in stdout
        the Rectangle instance with the character #
        """
        row = '#' * self.__width + ' ' * self.__x
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(row)

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
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
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
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
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
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
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
        if type(y) != int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
