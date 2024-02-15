#!/usr/bin/python3
"""Python module for lookup function"""


def lookup(obj):
    """Finds available attributes of obj
    Args:
        obj (object): object to lookup
    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
