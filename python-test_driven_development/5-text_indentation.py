#!/usr/bin/python3
"""This module provides a function that prints indented text."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    current = ""
    for char in text:
        current += char
        if char in ".?:":
            print(current.strip())
            print()
            current = ""
    if current.strip():
        print(current.strip(), end="")
