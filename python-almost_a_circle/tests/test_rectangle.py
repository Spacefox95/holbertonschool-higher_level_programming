#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test the Rectangle class
    """
    def test_rectangle_exist_0(self):
        """
        Test Rectangle inheritance from Base
        """
        r1 = Rectangle(1, 2)
        self.assertIsNotNone(r1)

    def test_rectangle_exist_1(self):
        """
        Test Rectangle inheritance from Base
        """
        r1 = Rectangle(1, 2, 3)
        self.assertIsNotNone(r1)

    def test_rectangle_exist_2(self):
        """
        Test Rectangle inheritance from Base
        """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r1)
    
    def test_rectangle_exist_3(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
    
    def test_rectangle_exist_4(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")

    def test_rectangle_exist_5(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "3")

    def test_rectangle_exist_6(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")
