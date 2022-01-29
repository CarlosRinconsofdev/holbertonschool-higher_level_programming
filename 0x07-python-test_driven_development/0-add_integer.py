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
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b