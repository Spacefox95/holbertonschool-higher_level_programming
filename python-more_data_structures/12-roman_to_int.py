#!/usr/bin/python3
def roman_to_int(roman_string):
    a = 0
    if roman_string:
        num = {'I': 1, 'V': 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in roman_string:
            for key in num:
                if i == key:
                    a += num.get(key)
        return a
    else:
        return 0
