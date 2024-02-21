#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test the Base class
    """
    def test_assign_id(self):
        """
        Test Base instantation
        """
        b1 = Base()

        self.assertEqual(b1.id, 1)

    def test_incrementation(self):
        """
        Test Base incrementation
        """
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_assignement_89(self):
        """
        Test Base assignement
        """
        b4 = Base(89)
        self.assertEqual(b4.id, 89)

