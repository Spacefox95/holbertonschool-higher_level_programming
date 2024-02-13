#!/usr/bin/python3
"""
===========================
Create a BaseGeometry class
===========================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
