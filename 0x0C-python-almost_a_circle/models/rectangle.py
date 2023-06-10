#!/usr/bin/python3


class Rectangle(Base):
    """New Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/gets width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Sets/gets height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Sets/gets x value of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Sets/gets y value of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
