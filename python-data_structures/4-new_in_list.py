#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list.copy()
    if idx >= 0 and idx < len(list):
        list[idx] = element
    return list
