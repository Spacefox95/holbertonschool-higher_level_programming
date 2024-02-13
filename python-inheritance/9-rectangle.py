#!/usr/bin/python3


"""
Create a BaseGeometry class
"""


class BaseGeometry:
    """
    For now, an empty class
    """
    def area(self):
        """
        For now, just raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check is the value is correct
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    New class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle class:
        - width(int) is a private instance
        - height(int) is a private instance
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print a rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
