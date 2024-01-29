#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ((tuple_a + (0, 0))[0] + (tuple_b + (0, 0))[0],
           (tuple_a + (0, 0))[1] + (tuple_b + (0, 0))[1])
    return res
