#!/usr/bin/python3

''' 11. Square #2'''

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description in the specified format"""
        return "[Square] {}/{}".format(self.__size, self.__size)

