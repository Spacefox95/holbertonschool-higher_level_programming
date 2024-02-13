#!/usr/bin/python3


"""
Class MyList inherits from list
Method:
print_sorted
"""


class MyList(list):
    """
    Print a sorted list of the list class
    """
    def print_sorted(self):
        liste = sorted(self)
        print(liste)
