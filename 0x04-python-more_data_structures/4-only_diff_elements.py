#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_in_one_set = set_1.symmetric_difference(set_2)
    return only_in_one_set
