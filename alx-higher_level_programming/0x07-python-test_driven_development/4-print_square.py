#!/usr/bin/python3
"""
This module has a function that prints a square using #
"""


def print_square(size):
    """prints a square using #

    Args:
        size (int): square size
    Returns:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("{} must be >= 0".format("size"))
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
