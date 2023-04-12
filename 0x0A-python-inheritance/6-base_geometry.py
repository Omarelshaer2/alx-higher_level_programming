#!/usr/bin/python3
"""
This module features a function called is_same_class
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
