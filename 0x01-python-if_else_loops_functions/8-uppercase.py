#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= ord('a') and  c <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
        print("")
