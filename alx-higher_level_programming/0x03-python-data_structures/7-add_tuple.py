#!/usr/bin/python3

def get_value(tup, index):
    try:
        return (tup[index])
    except IndexError:
        return (0)


def add_tuple(tuple_a=(), tuple_b=()):
    """Add tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        The return value. A tuple with 2 integers (add
        corresponding values):
    """
    new = []
    for i in [tuple_a, tuple_b]:
        new.append((get_value(i, 0), get_value(i, 1)))
    return ((new[0][0] + new[1][0], new[0][1] + new[1][1]))
