#!/usr/bin/python3
"""
Module containing subclass Mylist
of parent class list
"""


class MyList(list):
    """Sub-class of parent class list"""

    def print_sorted(self):
        """Functiom to print the list"""
        print(sorted(self))
