#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix and return a new matrix."""
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or matrix == []:
        raise TypeError(error)

    row_size = None
    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(error)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(error)

    return [[round(value / div, 2) for value in row] for row in matrix]
