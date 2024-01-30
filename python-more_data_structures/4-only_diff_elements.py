#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set()
    for i in set_1:
            if i not in set_2:
                diff_set.add(i)
    for j in set_2:
            if j not in set_1:
                diff_set.add(j)
    return diff_set
