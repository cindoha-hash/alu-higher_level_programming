#!/usr/bin/python3
"""This module provides a function that divides a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by div."""
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or matrix == []:
        raise TypeError(err)

    row_len = None
    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(err)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(err)

    return [[round(value / div, 2) for value in row] for row in matrix]
