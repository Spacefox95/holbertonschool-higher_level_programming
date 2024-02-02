#!/usr/bin/python3
print_sorted_dictionary = __import__('test').print_dict

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
