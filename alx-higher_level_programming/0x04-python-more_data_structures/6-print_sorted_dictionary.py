#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary.keys())
    lst.sort()
    newdict = {ky: a_dictionary[ky] for ky in lst}
    for k, v in newdict.items():
        print("{}: {}".format(k, v))
