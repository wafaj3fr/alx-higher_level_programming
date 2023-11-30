#!/usr/bin/python3

if __name__ == "__main__":
    """Print the summation, subtraction, multiplication and division of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    print("{} = {} = {}".format(a, b, calculator.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator.div(a, b)))
