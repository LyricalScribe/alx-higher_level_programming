#!/usr/bin/python3

"""Prints file to stdout"""


def read_file(filename=""):
    """Function to read a file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
