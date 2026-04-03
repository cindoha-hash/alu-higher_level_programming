#!/usr/bin/python3
"""Module for printing text with indentation after punctuation."""


def text_indentation(text):
    """Print text with two new lines after ., ? and :."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip(), end="")
