#!/usr/bin/python3
"""Returns object for json serialization"""


def class_to_json(obj):
    """a function to serialize obj"""
    my_dict = {}
    for key, value in obj.__dict__.items():
        my_dict[key] = value
    return my_dict
