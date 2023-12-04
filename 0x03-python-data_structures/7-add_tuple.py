#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    padded_tuple_a = tuple_a + (0, 0)
    padded_tuple_b = tuple_b + (0, 0)

    addition_result = (padded_tuple_a[0] + padded_tuple_b[0], padded_tuple_a[1] + padded_tuple_b[1])
    return addition_result
