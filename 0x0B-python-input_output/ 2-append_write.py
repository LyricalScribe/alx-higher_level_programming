#!/usr/bin/python3
"""Appends characters to a file"""


def append_write(filename="", text=""):
    """Function to append text to a file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
