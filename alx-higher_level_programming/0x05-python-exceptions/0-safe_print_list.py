#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for n, i in enumerate(my_list[0: x]):
            print(i, end="")
        print("")
        return (n + 1)
    except (IndexError, UnboundLocalError):
        return (0)
