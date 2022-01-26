#!/usr/bin/python3
"""class with no class or object attribute"""


class LockedClass:
    """
    prevents the user from dynamically creating
    new instance attributes called first_name
    """
    __slots__ = ['first_name']
