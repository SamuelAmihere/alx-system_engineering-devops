#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import (
            add, sub, mul, div)

    av = sys.argv[1:]

    if len(av) != 3:
        print("{}".format(
            "Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    ops = [('+', add), ('-', sub), ('*', mul), ('/', div)]
    not_found = True

    for op in ops:
        if op[0] == av[1]:
            not_found = False
            print("{} {} {} = {}".format(
                av[0], op[0], av[2],
                op[1](int(av[0]), int(av[2]))))

    if not_found:
        print("{}".format(
            "Unknown operator. Available operators: +, -, * and /"))
        exit(1)
