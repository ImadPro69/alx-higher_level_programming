#!/usr/bin/python3

class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        '''Initializing atributes'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description in the specified format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

