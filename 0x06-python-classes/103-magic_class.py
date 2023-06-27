#!/usr/bin/python3
"""This MagicClass implementation corresponds to a specific bytecode provided."""

import math

class MagicClass:
    """A Circle"""
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
