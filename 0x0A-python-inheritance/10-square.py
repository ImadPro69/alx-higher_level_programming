#!/usr/bin/python3
''' 10. Square #1'''

class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

