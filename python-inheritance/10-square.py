#!/usr/bin/python3
"""
===========================
Create a BaseGeometry class
===========================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    New class for square
    """

    def __init__(self, size):
        """
        Initialize size
        Check integer
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Correct output for square
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
