#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic math operations."""
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv[1:]) - 1 != 3:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        exit(1)

    a = int(arg[1])
    op = argv[2]
    b = int(argv[3])
    match op:
        case '+':
            print("{} + {}= {}".format(a, b, add(a, b)))
        case '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        case other:
            print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
