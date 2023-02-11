#!/usr/bin/python3

""" module of a Rectangle """

class Rectangle:
    """ created a Rectangle class """
    
    def __init__(self,width=0 , height=0):
        """ initializing data """
        self.__width = width
        self.__height = height
        
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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
            
    def area(self):
        """ sets the area of the instance """
        return self.__width * self.__height
        
    def perimeter(self):
        """ sets the perimeter of the instance"""
        return 2*(self.__width + self.__height)
         
        
        
    
    