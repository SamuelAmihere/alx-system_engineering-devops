#!/usr/bin/python3
"""A pyhton module that defines functions for maths operations

   matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix
       Args:
           matrix (list): A list of lists of integers or floats
           div (int/float): A number to divide the matrix by
       Returns:
           A new matrix with the result of the division
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(col / div, 2) for col in row] for row in matrix]
