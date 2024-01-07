#!/usr/bin/python3
"""matrix multiplication fonction"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    list of lists: The resulting matrix.
    """
    validate_matrix(m_a, 'm_a')
    validate_matrix(m_b, 'm_b')

    validate_matrix_multiplication(m_a, m_b)

    result_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return result_matrix


def validate_matrix(matrix, matrix_name):
    """
    Validate the matrix for the specified requirements.

    Parameters:
    - matrix (list of lists): The matrix to be validated.
    - matrix_name (str): The name of the matrix (used in error messages).

    Returns:
    None
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{matrix_name} must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{matrix_name} must be a list of lists")

    if not matrix or any(not row for row in matrix):
        raise ValueError(f"{matrix_name} can't be empty")

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(f"{matrix_name} should contain only integers or floats")


def validate_matrix_multiplication(m_a, m_b):
    """
    Validate matrices for multiplication.

    Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    None
    """
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("Each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("Each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
