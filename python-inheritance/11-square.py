#!/usr/bin/python3


"""
===========================
Create a BaseGeometry class
===========================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===========================
Create a BaseGeometry class
===========================
"""
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
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Correct output for square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__size * self.__size
