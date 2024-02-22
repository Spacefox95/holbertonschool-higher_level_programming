#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
import io
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

    def test_display_exist_without_x_y(self):
        """
        Test the display function
        """
        r1 = Rectangle(3, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                r1.display()
        captured_output = mock_stdout.getvalue()
        expected_output = "###\n###\n"
        self.assertEqual(captured_output, expected_output)

    def test_display_exist_without_y(self):
        """
        Test the display function
        """
        r1 = Rectangle(3, 2, 1)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                r1.display()
        captured_output = mock_stdout.getvalue()
        expected_output = " ###\n ###\n"
        self.assertEqual(captured_output, expected_output)


    def test_display_exist(self):
        """
        Test the display function
        """
        r1 = Rectangle(3, 2, 1, 1)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                r1.display()
        captured_output = mock_stdout.getvalue()
        expected_output = "\n ###\n ###\n"
        self.assertEqual(captured_output, expected_output)

    def test_to_dictionary(self):
        """
        Test the function that return a dict representation of rectangle
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'id': 21, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_to_update(self):
        """
        Test the update function
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=0, width=0, height=0, x=0, y=0)
        self.assertEqual(r1.id, 0)
        self.assertEqual(r1.width, 0)
        self.assertEqual(r1.height, 0)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
