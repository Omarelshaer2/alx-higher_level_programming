#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class to represent a rectangle object.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object.

        :param width: An integer representing the width of the rectangle.
        :param height: An integer representing the height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        :return: An integer representing the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: An integer representing the width of the rectangle.
        :raise TypeError: If value is not an integer.
        :raise ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        :return: An integer representing the height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: An integer representing the height of the rectangle.
        :raise TypeError: If value is not an integer.
        :raise ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        :return: An integer representing the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: An integer representing the perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Get a string representation of the rectangle.

        :return: A string representing the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join("#" * self._width for _ in range(self._height))

    def __repr__(self):
        """
        Get a string representation of the rectangle that can be used to reproduce it.

        :return: A string representing the rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"
