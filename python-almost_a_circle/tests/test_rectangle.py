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
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_rectangle_exist_9(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_rectangle_exist_10(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_rectangle_exist_11(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_rectangle_exist_12(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -3)

    def test_rectangle_exist_13(self):
        """
        Test Rectangle inheritance from Base
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)

    def test_area_exist(self):
        """
        Test the area function
        """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)

    def test_str_exist(self):
        """
        Test the str return
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6' )

    def test_display_without_x_y(self):
        """Test display() whihout x and y"""
        r1 = Rectangle(1, 2)
        expected_output = "#\n#\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)

    def test_display_without_y(self):
        """Test display() whitout y"""
        r1 = Rectangle(1, 2, 1)
        expected_output = " #\n #\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)

    def test_display(self):
        """Test display() whitout y"""
        r1 = Rectangle(1, 2, 1, 1)
        expected_output = "\n #\n #\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)
    
    def test_to_dictionary(self):
        """
        Test the function that return a dict representation of rectangle
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'id': 23, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        """
        Test the that the update function exist
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_create(self):
        """
        Test that the create function exist
        """
        r1 = Rectangle(id=89, width=1, height=2, x=3, y=4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_save_to_file_none(self):
        """
        Test that the save to file works correctly
        """
        filename = "Rectangle.json"
        Rectangle.save_to_file(None)
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
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            list_output = json.load(f)
        expected_output = []
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertEqual(list_output, expected_output)
        os.remove(filename)
    
    def test_save_to_file_full(self):
        """
        Test that the save to file works correctly
        """
        filename = "Rectangle.json"
        Rectangle.save_to_file([Rectangle(1, 2)])
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
        Rectangle.save_to_file(list_rectangles_input)
        Rectangle.load_from_file()
        self.assertTrue(os.path.exists("Rectangle.json"))
