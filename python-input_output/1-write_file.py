#!/usr/bin/python3
"""
Write a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        b = f.write(text)
        return b
