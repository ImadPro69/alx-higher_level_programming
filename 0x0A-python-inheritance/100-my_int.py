#!/usr/bin/python3
''' 12. My integer'''

class MyInt(int):
    '''class MyInt'''
    def __eq__(self, other):
        """Override the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator"""
        return super().__eq__(other)

