#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    i = a_dictionary.get(key)
    if (i):
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return a_dictionary
