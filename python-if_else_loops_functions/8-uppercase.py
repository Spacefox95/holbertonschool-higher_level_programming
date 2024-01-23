#!/usr/bin/python3
def uppercase(str):
    buffer = ""
    for i in str:
        j = ord(i)
        if 97 <= j <= 122:
            buffer += chr(j - 32)
        else:
            buffer += i
    print("{}".format(buffer))
