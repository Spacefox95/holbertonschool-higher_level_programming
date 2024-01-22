#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {}".format(number), end=" ")
if (number > 0):
    if (number % 10) > 5:
        print("is {} and is greater than 5".format(number % 10))
    elif (number % 10) == 0:
        print("is {} and is 0".format(number % 10))
    else:
        print("is {} and is less than 6 and not 0".format(number % 10))
if (number < 0):
    number = number * -1
    if (number % 10) == 0:
        print("is {} and is 0".format(number % 10))
    else:
        print("is -{} and is less than 6 and not 0".format(number % 10))
