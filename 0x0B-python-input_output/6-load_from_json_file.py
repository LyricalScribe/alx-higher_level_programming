#!/usr/bin/python3
"""Reads from a jason file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
