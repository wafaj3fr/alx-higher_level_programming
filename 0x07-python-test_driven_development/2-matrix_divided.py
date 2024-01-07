#!/usr/bin/python3
""" matrix divided """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
