#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
import json
import sys
import os


from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string_None(self):
        """
        Test Base JSON string representation of None
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_empty(self):
        """
        Test Base JSON string representation of empty bracket
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_full(self):
        """
        Test Base JSON string representation of full bracket
        """
        json_dictionary = Base.to_json_string([ { 'id' : 12}])
        self.assertEqual(json_dictionary, '[{"id": 12}]')

    def test_from_json_string_None(self):
        """
        Test Base for None list of the JSON string representation
        """
        json_list_input = Base.to_json_string(None)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """
        Test Base for empty list of the JSON string representation
        """
        json_list_input = Base.to_json_string([])
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_from_json_string_full(self):
        """
        Test Base for full list of the JSON string representation
        """
        json_list_input = Base.to_json_string('[{ "id": 89 }]')
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, '[{ "id": 89 }]')

if __name__ == "__main__":
    unittest.main()
