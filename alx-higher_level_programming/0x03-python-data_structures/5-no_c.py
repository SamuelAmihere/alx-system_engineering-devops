#!/usr/bin/python3
def no_c(my_string):

    arr = ["" if s in ['c', 'C'] else s for s in my_string]
    return ("".join(arr))
