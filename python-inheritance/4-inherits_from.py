#!/usr/bin/python3


"""
Check that the object is an instance of a specified class
Return True if true, else False
"""


def inherits_from(obj, a_class):
    """
    Return the type of the object
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
