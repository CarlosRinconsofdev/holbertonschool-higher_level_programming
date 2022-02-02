#!/usr/bin/python3
"""
``load_from_json_file`` Function
"""


import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    """
    with open(filename, mode='r') as file:
        return (json.loads(file.read()))
