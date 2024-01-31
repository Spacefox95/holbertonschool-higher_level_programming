#!/usr/bin/python3
def safe_print_integer(value):
    if value:
        try:
            print("{:d}".format(value))
            return True
        except (ValueError, TypeError, SyntaxError):
            return False
    else:
        return False
