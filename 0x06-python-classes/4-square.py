#!/usr/bin/python3
""" class that defines a square"""


class Square:
    """ Atributes: size (int): the size of the square """
    def __init__(self, size=0):
        """Initializes method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size*self.__size

    @property
    def size(self):
        """Check property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets for size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
