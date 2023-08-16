#!/usr/bin/python3
'''Here We Learn More About Classes and Objects'''
class Rectangle:
    '''Class Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializing atributes'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Getting The Value Of Width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setting The Value Of Width'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getting The Value Of Height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setting The Value Of Height'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Defining a Method To Get The Area Of The Rectangle'''
        return (self.height * self.width)

    def perimeter(self):
        '''Defining a Method To Get The Perimeter Of The Rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.height + self.width) * 2)
