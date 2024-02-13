#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of available attributes and method of an object
    """
    return list(dir(obj))
