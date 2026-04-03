#!/usr/bin/python3
"""Module for printing a square of # characters."""


def print_square(size):
    """Print a square with the character #."""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int] or type(size) is bool:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
