#!/usr/bin/python3
"""A pyhton module that defines functions for maths operations

   add_integer: adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): first integer
        b (int): second integer

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: the sum of a and b
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
