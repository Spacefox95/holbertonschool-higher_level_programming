#!/usr/bin/python3
"""
Create a new class Rectangle, that inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    A new Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle class
        Parameters :
        - width
        - height
        - x
        - y
        - id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


@property
def width(self):
    """
    Getter
    Return private instance attribute width
    """
    return self.__width


@property
def height(self):
    """
    Getter
    Return private instance attribute height
    """
    return self.__height


@property
def x(self):
    """
    Getter
    Return private instance attribute x
    """
    return self.__x


@property
def y(self):
    """
    Getter
    Return private instance attribute y
    """
    return self.__y


@width.setter
def width(self, value):
    """
    Setter
    Arg = width : set width
    """
    self.__width = value


@height.setter
def height(self, value):
    """
    Setter
    Arg = height : set height
    """
    self.__height = value


@x.setter
def x(self):
    """
    Setter
    Arg = x : set x
    """
    self.__x = x


@y.setter
def y(self):
    """
    Setter
    Arg = y : set y
    """
    self.__y = y
