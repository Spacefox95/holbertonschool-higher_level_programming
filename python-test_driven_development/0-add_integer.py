#!/usr/bin/python3
"""
add_integer = __import__('0-add_integer').add_integer
create a add_integer variable
import add_integer function
"""


def add_integer(a, b=98):
    """
    add_integer: add two integer of floats; if floats, casted in int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
