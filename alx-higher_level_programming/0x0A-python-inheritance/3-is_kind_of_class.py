#!/usr/bin/python3
"""Module for is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if the object is
    an instance

    Args:
        obj: object to check its instance
        a_class (type): the class to match the type of obj to

    Returns:
        bool: True if obj is an instance of a_class, False otherwise
    """
    if not isinstance(obj, a_class):
        return False
    return True
