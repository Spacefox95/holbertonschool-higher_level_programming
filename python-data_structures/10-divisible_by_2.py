#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean = []
    for i in range(len(my_list)):
        boolean.append(i % 2 == 0)
    return boolean
