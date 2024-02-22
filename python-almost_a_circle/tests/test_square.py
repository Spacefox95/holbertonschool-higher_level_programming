#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
import json
import sys
import os


from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test the Rectangle class
    """
    def test_square_exist_0(self):
        """
        Test Rectangle inheritance from Base
        """
        s1 = Square(1)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.size, 1)

    def test_square_exist_1(self):
        """
        Test Rectangle inheritance from Base
        """
        s1 = Square(1, 2)
        self.assertIsInstance(s1, Square)
        self.assertIsNotNone(s1)
    
    def test_square_exist_2(self):
        """
        Test Rectangle inheritance from Base
        """
        s1 = Square(1, 2, 3)
        self.assertIsNotNone(s1)
    
    def test_square_exist_3(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            s1 = Square("1")

    def test_square_exist_4(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            s1 = Square(1, "2")

    def test_square_exist_5(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, "3")

    def test_square_exist_6(self):
        """
        Test Rectangle inheritance from Base
        """
        s1 = Square(1, 2, 3, 4)
        self.assertIsNotNone(s1)

    def test_square_exist_7(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            s1 = Square(-1)
    
    def test_square_exist_8(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            s1 = Square(1, -2)
    
    def test_square_exist_7(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            s1 = Square(1, 2, -3)

    def test_square_exist_7(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            s1 = Square(0)
    
    def test_str_exist(self):
        """
        Test the str return
        """
        s1 = Square(4, 6, 2, 1)
        self.assertEqual(s1.__str__(), '[Square] (1) 6/2 - 4' )