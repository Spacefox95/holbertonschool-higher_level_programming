#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = 0
    args = sys.argv[1:]
    for i in args:
        c += int(i)
print("{}".format(c))
