#!/usr/bin/python3
""" 8. Rectangle"""

class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

