#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    # Use dir() to get the list of names
    names = dir(obj)

    # Filter out attributes and methods that are not callable
    result = [name for name in names if callable(getattr(obj, name))]

    return result

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
