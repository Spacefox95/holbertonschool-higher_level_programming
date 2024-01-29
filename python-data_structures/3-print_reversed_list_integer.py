#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    while my_list:
        print("{:d}".format(my_list.pop()))
