#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    operator = argv[2]
    math = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in math:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, math[operator](a, b)))
