#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        list = my_list.copy()
        if idx < 0 or idx > len(list):
            return list
        else:
            list[idx] = element
            return list
