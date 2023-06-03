#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """dDfines a square class"""

    def __init__(self, size):
        """Initializes a new rectangle"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
