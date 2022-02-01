#!/usr/bin/python3
"""
``Mylist`` module
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        prints the list sorted
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
