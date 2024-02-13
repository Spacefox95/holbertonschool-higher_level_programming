#!/usr/bin/python3


"""
Create a BaseGeometry class
"""


class BaseGeometry:
    """
    For now, an empty class
    """

    def __init__(self):
        """
        Initialize the class
        """
        pass

    def area(self):
        """
        For now, just raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check is the value is correct
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
