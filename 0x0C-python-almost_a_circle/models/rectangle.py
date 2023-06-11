#!/usr/bin/python3

"""Defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """New Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new Rectangle

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
            id (int): The identity of the new Rectangle
        Raises:
            TypeError: If either width or height is not an int
            ValueError: If either width or height <= 0
            TypeError: If either x or y is not an int
            ValueError: If either x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/gets the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Sets/gets the height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets/gets the x value of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Sets/gets the y value of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Print Rectangle using the #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Rectangle updates;

        Args:
            *args (ints):
                - (1) argument represents id attribute
                - (2) argument represents width attribute
                - (3) argument represent height attribute
                - (4) argument represents x attribute
                - (5) argument represents y attribute
            **kwargs
        """
        if args:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a
