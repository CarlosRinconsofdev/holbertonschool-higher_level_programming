#!/usr/bin/python3
"""
``add_integer``
write a function that add_integers(a, b=98)
and return the sum.
"""


def add_integer(a, b=98):
    """Adds two integers:
        >>>my_function(2, 3)
        5"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
