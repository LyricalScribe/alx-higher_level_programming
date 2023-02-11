#!/usr/bin/python3

"""empty class Rectangle"""


class Rectangle:
    """ empty class Rectangle """

    def __init__ (self,width=0, height=0):
        """ initializing data """
        
        self.__height = height
        self.__width = width
        

    @property
    def width(self):
        """ sets the width of the instance """
        return self.__width
        
    @width.setter
    def width(self, value):
        """ gets the width of a rectangle class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            
            
    @property   
    def height(self):
        """ sets the height of the instance """
        return self.__height
        
    @height.setter
    def height(self, value):
        """ gets the height of a rectangle class """
        if type(value) is not int:
            raise TypeError("height must be an integer")  
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        
    