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
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

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

    def test_rectangle_exist_7(self):
        """
        Test Rectangle inheritance from Base
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)


    def test_rectangle_exist_8(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_exist_9(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_exist_10(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_exist_11(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_exist_12(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")