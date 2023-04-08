#!/usr/bin/python3
"""
Defines a function that multiplies 2 matrices using NumPy's matmul function.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the product of two matrices.

    Args:
        m_a (matrix): The first matrix.
        m_b (matrix): The second matrix.

   Returns:
        matrix: The resulting product of the two matrices.
    """
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
