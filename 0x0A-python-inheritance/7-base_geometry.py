#!/usr/bin/python3
"""Defines basegeometry class"""


class BaseGeometry:
    """Defines a class"""
    def area(self):
        """r
        Riases exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
