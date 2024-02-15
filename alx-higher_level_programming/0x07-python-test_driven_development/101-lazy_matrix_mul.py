#!/usr/bin/python3
"""A pyhton module for lazy_matrix_mul function"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Uses the NumPy module to multiply 2 matrices

    Args:
        m_a (list): First matrix
        m_b (list): Second matrix

    Returns:
        list: New matrix
    """

    return np.matmul(m_a, m_b)
