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

    def check_value_input_for_w_h(self, value, attr_name):
        """
        Validator for input
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))
        else:
            return value

    def check_value_input_for_x_y(self, value, attr_name):
        """
        Validator for input
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))
        else:
            return value

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
        self.__width = self.check_value_input_for_w_h(value, "width")

    @height.setter
    def height(self, value):
        """
        Setter
        Arg = height : set height
        """
        self.__height = self.check_value_input_for_w_h(value, "height")

    @x.setter
    def x(self, value):
        """
        Setter
        Arg = x : set x
        """
        self.__x = self.check_value_input_for_x_y(value, "x")

    @y.setter
    def y(self, value):
        """
        Setter
        Arg = y : set y
        """
        self.__y = self.check_value_input_for_x_y(value, "y")
