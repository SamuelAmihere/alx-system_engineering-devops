#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for k, v in copy.items():
        if v == value:
            a_dictionary.pop(k, None)
    return a_dictionary
