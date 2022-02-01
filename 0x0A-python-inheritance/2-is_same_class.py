#!/usr/bin/python3
"""
``is_same_class`` module
"""


def is_same_class(obj, a_class):
    """
    If object is instance of a class return True, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
