#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints reversed form of a list of integers"""
    if my_list:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
    else:
        pass
