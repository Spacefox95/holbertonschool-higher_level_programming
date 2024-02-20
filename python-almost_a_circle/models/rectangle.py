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

    def area(self):
        """
        Return the area value of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Print in the stdout the Rectangle instance
        """
        for b in range(self.y):
            print()
        for i in range(self.height):
            for a in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Returns Rectangle carateristics
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assign an argument to each attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        elif args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            update_values = args[:len(attributes)]
            list(map(lambda attr, value: setattr
                     (self, attr, value), attributes, update_values))

    def to_dictionary(self):
        """
        Returns a dictionary representation of a rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

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
