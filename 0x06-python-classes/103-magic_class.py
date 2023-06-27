#!/usr/bin/python3
"""Define a MagicClass"""

import math
    """A Circle"""

class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        return self.radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius
