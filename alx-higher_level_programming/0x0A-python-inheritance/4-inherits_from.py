#!/usr/bin/python3
"""A module for inherits_from function"""


def inherits_from(obj, a_class):
    """Checks whether an object is an instance of
    a class that inherited
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
