#!/usr/bin/python3


"""
Write a class Rectangle that defines a rectangle:
* Private instance attribute: width
* Private instance attribute: height
* Instantiation with optional width and heigh
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns
the rectangle perimeter
* You are not allowed to import any module
"""


class Rectangle:
    """
    Class named Rectangle
    """
    number_of_instances = 0
    """
    public class attribute used to count the instances
    that are created or deleted
    """
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Use of the init method to create two private instance attributes

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property decorator to turn the width method into a getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter decorator allowing to modify the value of width method
        """
        if not isinstance(value, int):
            """
            Raising a TypeError exception as the width/value must be an integer
            """
            raise TypeError("width must be an integer")
        elif value < 0:
            """
            Raising a ValueError exception as the size/value must be >= 0
            """
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property decorator to turn the width method into a getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter decorator allowing to modify the value of width method
        """
        if not isinstance(value, int):
            """
            Raising a TypeError exception as the width/value must be an integer
            """
            raise TypeError("height must be an integer")
        elif value < 0:
            """
            Raising a ValueError exception as the size/value must be >= 0
            """
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area

        Returns:
            int: the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter

        Returns:
            int: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        String method that returns a value of type string

        Returns:
            str: the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(str(self.print_symbol) *
                             self.width for x in range(self.height))

    def __repr__(self):
        """
        String method that a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Del method that prints a message when an instance
        of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that that returns the biggest
        rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance
        """
        return cls(size, size)
