#!/usr/bin/python3
def no_c(my_string):
    return ("".join(c for c in my_string if c not in "Cc"))
