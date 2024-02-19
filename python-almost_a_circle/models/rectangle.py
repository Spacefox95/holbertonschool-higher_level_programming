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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)


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
def width(self):
    """
    Setter
    Arg = width : set width
    """
    self.__width = width


@height.setter
def height(self):
    """
    Setter
    Arg = height : set height
    """
    self.__height = height


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
