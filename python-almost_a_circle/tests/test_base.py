#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_assign_id(self):
        """
        Create instances of Base and assign to check id
        """
        obj_1 = Base()

        self.assertEqual(obj_1.id, 1)
