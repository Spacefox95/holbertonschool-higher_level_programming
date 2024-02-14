#!/usr/bin/python3
"""
Append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        b = f.write(text)
        return b
