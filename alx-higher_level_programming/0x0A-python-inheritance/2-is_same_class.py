#!/usr/bin/python3
"""A module for is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj: object to check its instance
        a_class (type): the class to match the type of obj to

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise"""
    return type(obj) is a_class
