#!/usr/bin/python3
"""``Student`` Class"""


class Student:
    """Public instance attributes
        first_name
        last_name
        age.
        Public method: def to_json(self, attrs=None)
    """

    def __init__(self, first_name, last_name, age):
        """Inithialization of the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves representation of a Student iinstance"""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
