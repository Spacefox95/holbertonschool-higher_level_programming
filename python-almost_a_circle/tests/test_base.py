#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_assign_id(self):
        """
        Create instances of Base and assign to check id
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base()
        self.assertEqual(b5.id, 4)
