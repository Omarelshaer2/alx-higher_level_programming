#!/usr/bin/python3
"""
This module defines a Rectangle class representing a two-dimensional rectangle
"""

class Rectangle:
    """
    A rectangle with a given width and height

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with a given width and height

        Args:
            width (int): The width of the rectangle (default 0)
            height (int): The height of the rectangle (default 0)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): The new width of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be non-negative")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): The new height of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be non-negative")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle

        Returns:
            str: A string representation of the rectangle
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
