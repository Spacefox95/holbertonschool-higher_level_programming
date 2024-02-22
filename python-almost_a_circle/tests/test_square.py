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
    
    def test_to_dictionary(self):
        """
        Test the function that return a dict representation of square
        """
        s1 = Square(10, 2, 1, 9)
        self.assertEqual(s1.to_dictionary(), {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        """
        Test the that the update function exist
        """
        r = Square(1, 2, 3, 4)
        r.update(id=6, size=7, x=9, y=10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.size, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)
    
    def test_create(self):
        """
        Test that the create function exist
        """
        r1 = Square(id=89, size=1, x=3, y=4)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.size, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_save_to_file_none(self):
        """
        Test that the save to file works correctly
        """
        filename = "Rectangle.json"
        Square.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            list_output = json.load(f)
        expected_output = []
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(list_output, expected_output)
        os.remove(filename)

    def test_save_to_file_empty(self):
        """
        Test that the save to file works correctly
        """
        filename = "Rectangle.json"

        Square.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, "r") as f:
            file_content = f.read()

        self.assertEqual(file_content, "[]")
        os.remove(filename)
    
    def test_save_to_file_full(self):
        """
        Test that the save to file works correctly
        """
        filename = "Rectangle.json"
        Square.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            list_output = json.load(f)
        expected_output = [{'id': 22, 'width': 1, 'height': 2, 'x': 0, 'y': 0}]
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(list_output, expected_output)
        os.remove(filename)

    def test_load_from_file_none(self):
        """"
        Test that the load file function works correctly
        """
        list_rectangles_input = None
        Square.save_to_file(list_rectangles_input)
        Square.load_from_file()
        self.assertTrue(os.path.exists("Rectangle.json"))
