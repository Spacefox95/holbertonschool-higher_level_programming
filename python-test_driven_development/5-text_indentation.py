#!/usr/bin/python3


"""
text_indentation = __import__('5-text_indentation').text_indentation
create a text_indentation variable
import text_indentation function
"""


def text_indentation(text):
    """
    text_indentation: prints a text and newline for every '.', '?' or ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    character = {'.', '?', ':'}
    line = ""

    for i in text:
        line += i
        if i in character:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
