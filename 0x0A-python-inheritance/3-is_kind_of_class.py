#!/usr/bin/python3
"""Defines a class and an inhertited function that checks a class"""


def is_kind_of_class(obj, a_class):
    """Checks if object is or is not an inherited instance"""

    return isinstance(obj, a_class)
