#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a geometric rectangle.
"""


class Rectangle:
    """
    A Rectangle object represents a 2D rectangle with a given width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        :param width: The width of the rectangle.
        :type width: int
        :param height: The height of the rectangle.
        :type height: int
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        :return: The width of the rectangle.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle to the given value.

        :param value: The new width of the rectangle.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        :return: The height of the rectangle.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle to the given value.

        :param value: The new height of the rectangle.
        :type value: int
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Returns the area of the rectangle.

        :return: The area of the rectangle.
        :rtype: int
        """
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        :rtype: int
        """
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)
