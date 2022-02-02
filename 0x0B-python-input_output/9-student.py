#!/usr/bin/python3
"""``Student`` Class"""


class Student:
    """Public instance attributes
        first_name
        last_name
        age.
        Public method: def to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """Inithialization of the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves representation of a Student iinstance"""
        return self.__dict__
