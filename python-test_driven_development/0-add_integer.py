#!/usr/bin/python3
"""Module for integer addition."""


def add_integer(a, b=98):
    """Add two integers after validating and casting floats."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
