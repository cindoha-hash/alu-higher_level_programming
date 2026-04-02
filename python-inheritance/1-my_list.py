#!/usr/bin/python3
"""Module that defines a custom list class."""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
