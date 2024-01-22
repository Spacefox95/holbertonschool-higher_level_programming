#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
if (number > 0):
    o = number % 10
    if (o) > 5:
        print("{} and is greater than 5".format(o))
    elif (o) == 0:
        print("{} and is 0".format(o))
    else:
        print("{} and is less than 6 and not 0".format(o))
if (number < 0):
    number = number * -1
    o = number % 10
    print("-{} and is less than 6 and not 0".format(o))
