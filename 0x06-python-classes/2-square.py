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
            self._size = size
