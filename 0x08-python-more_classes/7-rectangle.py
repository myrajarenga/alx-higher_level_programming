#!/usr/bin/python3

"""
empty class rectangle
"""


class Rectangle:
    """
    Rectangle empty class
    """

    number_of_instances = 0
    print_symbol = "#"
    print_symbol = "&"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            if i != self.__height - 1:
                string = string + "#" * self.__width + "\n"
            else:
                string = string + "#" * self.__width
        return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
