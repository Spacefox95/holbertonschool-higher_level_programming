#!/usr/bin/python3
"""
Create a new class Square, that inherits from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A new Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square class
        Parameters :
        - size
        - x
        - y
        - id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns Square carateristics
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter
        Return public instance attribute size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter
        Arg = value : set value(size) = width = height
        """
        self.width = value
        self.height = value
        self.check_value_input_for_w_h(value, "width")
