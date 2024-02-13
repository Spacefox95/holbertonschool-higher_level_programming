#!/usr/bin/python3


"""
Just a function to check attributes and method
"""


def lookup(obj):
    """
    Return a list of available attributes and method of an object
    """
    liste = []
    for i in dir(obj):
        liste.append(i)
    return liste
