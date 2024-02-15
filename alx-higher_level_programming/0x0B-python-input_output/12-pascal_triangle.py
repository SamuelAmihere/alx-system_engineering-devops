#!/usr/bin/python3
"""A module with pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle
    """
    if n <= 0:
        return []
    pt = []
    for i in range(n):
        if i == 0:
            pt.append([1])
        elif i == 1:
            pt.append([1, 1])
        else:
            row = [1]
            for j in range(1, i):
                sum_above = pt[i-1][j-1] + pt[i-1][j]
                row.append(sum_above)
            row.append(1)
            pt.append(row)
    return pt
