#!/usr/bin/pyhton3


"""
Module containing function to check if an object is the instance
of a class or the class it inherits from
"""


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is the instance
      6 of a class or the class it inherits from

    Arg:
        obj: Object of a_class
        a_class: class

    Return:
        True
        False
    """
    if isinstance(obj, a_class):
        return True
    return False
