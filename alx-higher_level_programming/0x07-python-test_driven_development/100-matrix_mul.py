#!/usr/bin/python3
"""A pyhton module that defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): The first matrix
        m_b (list): The second matrix
    Returns:
        list: The result of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("{} can't be empty".format(
            "m_a" if len(m_a) == 0 else "m_b"))
    if len(m_a[0]) == 0 or len(m_b[0]) == 0:
        raise ValueError("{} can't be empty".format(
            "m_a" if len(m_a[0]) == 0 else "m_b"))

    # test for rectangularity
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # multiplication impossible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)] for row_a in m_a]


if __name__ == "__main__":
    """Test cases"""
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
