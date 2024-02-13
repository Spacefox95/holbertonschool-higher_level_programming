#!/usr/bin/python3
"""
Open and read a file
"""


def read_file(filename=""):
    """
    Open and read a file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
