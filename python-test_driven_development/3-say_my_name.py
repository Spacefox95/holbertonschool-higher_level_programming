#!/usr/bin/python3
"""
say_my_name = __import__('3-say_my_name').say_my_name
create a say_my_name variable
import say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: print first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
