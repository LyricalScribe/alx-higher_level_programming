#!/usr/bin/python3
""" this module represents a class square """


class Square:
    """Represents a square class """
    def __init__(self, size=0):
        """Initialize data"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of a square """
        return (self.__size * self.__size)
