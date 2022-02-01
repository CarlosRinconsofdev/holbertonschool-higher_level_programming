#!/usr/bin/python3
"""
``is_same_class`` module
"""


def is_same_class(obj, a_class):
    """
    If object is instance of a class return True, otherwise False
    """
    if not isinstance(a_class, type):
        return False
    else:
        return True
