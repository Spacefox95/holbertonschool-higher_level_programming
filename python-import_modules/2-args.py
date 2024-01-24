#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args = sys.argv[1:]
p = 1
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for i in args:
    print("{}: {}".format(p, i))
    p += 1
