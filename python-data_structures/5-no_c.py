#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    nul = ""
    for i in new_string:
        if i != 'c' and i != 'C':
            nul += i
    return nul
