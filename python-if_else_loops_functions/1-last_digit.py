#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_copy = number
o = 0
print("Last digit of {} is".format(number), end=" ")
if number < 0:
    number_copy *= -1
    o = -1 * (number_copy % 10)
else:
    o = number % 10
if o > 5:
    print(f"{o} and is greater than 5")
elif o == 0:
    print(f"{o} and is 0")
else:
    print(f"{o} and is less than 6 and not 0")
