#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    result = 0
    if argv[2] == '+':
        result = add(a, b)
    elif argv[2] == '-':
        result = sub(a, b)
    elif argv[2] == '*':
        result = mul(a, b)
    elif argv[2] == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /".format())
        exit(1)
    print("{} {} {} = {}".format(a, argv[2], b, result))
