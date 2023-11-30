#!/usr/bin/python3
import sys

def sum_arguments():
    arguments = sys.argv[1:]
    result = sum(int(arg) for arg in arguments)
    print(result)

sum_arguments()
