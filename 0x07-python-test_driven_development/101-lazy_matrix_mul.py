#!/usr/bin/python3
"""lazy matrix multiplication"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    list of lists: The resulting matrix.
    """
    # Convert matrices to NumPy arrays
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    result_matrix = np.dot(np_m_a, np_m_b)

    # Convert the result back to a list of lists
    result_matrix_list = result_matrix.tolist()

    return result_matrix_list
