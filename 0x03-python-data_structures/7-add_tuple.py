#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a)):
        for j in range(len(tuple_b)):
            if i == j:
                a = tuple_a[0] + tuple_b[0]
                b = tuple_b[1] + tuple_a[1]
    print("({}, {})".format(a, b))
