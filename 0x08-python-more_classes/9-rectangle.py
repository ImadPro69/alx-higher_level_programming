#!/usr/bin/python3
"""A square is a Rectangle"""
class Rectangle:
    """Defines a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the Data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a Value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the Position"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a Value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current rectangle Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return a string with rectangle to Stdout"""
        if self.__height == 0 or self.__width == 0:
            return ''
        _str = ""
        for i in range(self.__height):
            _str += str(self.print_symbol) * self.__width
            if self.height != i + 1:
                _str += '\n'
        return _str

    def __repr__(self):
        """Return a string representation of the Rectangle"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints the Message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the Area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with Width == height == size"""
        width = size
        heidht = size
        return cls(width, heidht)
