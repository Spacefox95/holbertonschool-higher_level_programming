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
        self.assertIsNotNone(s1)
    
    def test_square_exist_2(self):
        """
        Test Rectangle inheritance from Base
        """
        s1 = Square(1, 2, 3)
        self.assertIsNotNone(s1)
    


    