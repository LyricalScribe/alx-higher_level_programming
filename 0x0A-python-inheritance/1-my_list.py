#!/usr/bin/python3
"""Defines an inherited list class"""


class MyList(list):
    """A class for sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order"""
        print(sorted(self))
