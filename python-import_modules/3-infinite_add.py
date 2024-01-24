#!/usr/bin/python3
import sys
c = 0
i = 0
b = 0
args = sys.argv[1:]
for i in args:
    c += int(i)
print("{}".format(c))
