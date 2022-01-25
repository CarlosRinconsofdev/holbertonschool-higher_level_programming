#!/usr/bin/python3
"""
add_integer:
write a function that adds 2 integers (a, b)
and return the sum.
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): integer to add
        b (int): integer to add

    Raise:
        TypeError: exception with the message.
    """

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
