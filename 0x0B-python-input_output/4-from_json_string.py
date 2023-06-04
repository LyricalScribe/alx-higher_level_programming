#!/usr/bin/python3
"""Return a python object from json string"""
import json


def from_json_string(my_str):
    """Returns python object from a jason string"""

    return json.loads(my_str)
