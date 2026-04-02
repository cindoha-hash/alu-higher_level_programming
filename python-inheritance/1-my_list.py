#!/usr/bin/python3
"""Module that defines a custom list class."""


class MyList(list):
    """Custom list that inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
