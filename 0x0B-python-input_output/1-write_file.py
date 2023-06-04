#!/usr/bin/python3

"""Writes to a file"""


def write_file(filename="", text=""):
    """Function to write to a file and
    return number of written charcaters"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
