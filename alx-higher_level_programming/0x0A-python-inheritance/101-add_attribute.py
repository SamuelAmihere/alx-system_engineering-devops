#!/usr/bin/python3
"""Module with a function that adds a new attribute to an
   object if it's possible
"""


def has_attribute(obj, name):
    """Checks if an object has an attribute
    Args:
        obj (object): object to check
        name (str): attribute's name
    Returns:
        bool: True if it has the attribute, False otherwise
    """
    if (hasattr(obj, "__slots__") and name in obj.__slots__) or\
            hasattr(obj, "__dict__"):
        return True
    return False


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible
    Args:
        obj (object): object to add attribute to
        name (str): attribute's name
        value (any): attribute's value
    Raises:
        TypeError: 'if object can't have new attribute'
    """
    if not has_attribute(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
