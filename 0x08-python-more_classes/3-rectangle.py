#!/usr/bin/python3

""" module of a Rectangle """

class Rectangle:
    """ created a Rectangle class """
    
    def __init__(self, width=0, height=0):
        """ initializing data """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """ sets the width of the instance """
        return self.___width
        
    @width.setter
    def width(self, value):
        """ gets the width of a rectangle class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.___width = value
            
    @property
    def height(self):
        """ sets the width of the instance """
        return self.__height
        
    @height.setter
    def height(self, value):
        """ gets the width of a rectangle class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
            
    def area(self):
        """ return the area of the rectangle """
        return self.___width * self.__height
        
    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.___width == 0 or self.__height == 0:
            return 0
        return 2*(self.___width + self.__height)
        
    def __str__(self):
        """ prints string representation of rectangle class """
        if self.___width == 0 or self.__height == 0:
            return ' '
        else:
            hashes = '#' *self.___width
            return '\n'.join(hashes for h in range(self.__height))
     