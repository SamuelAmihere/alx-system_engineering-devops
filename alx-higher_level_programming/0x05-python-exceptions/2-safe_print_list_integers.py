#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n, c = 1, 0
    while (n <= x):
        try:
            print("{:d}".format(my_list[n - 1]), end="")
            c += 1
        except (ValueError, TypeError):
            ...
        n += 1

    print("")
    return (c)
