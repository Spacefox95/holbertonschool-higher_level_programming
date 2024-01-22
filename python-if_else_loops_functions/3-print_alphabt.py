#!/usr/bin/python3
for a in range(97, 123):
    if a not in [101, 113]:
        print("{:c}".format(a), end="")
