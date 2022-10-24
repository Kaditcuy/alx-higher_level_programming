#!/usr/bin/pyhton3
"""Module 3-is_kind_of_class containins function to check"""


def is_kind_of_class(obj, a_class):
    """
        Function that checks if an object is the instance
        of a class or a parent class
    """
    if isinstance(obj, a_class):
        return True
    return False
