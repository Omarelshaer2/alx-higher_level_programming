#!/usr/bin/python3
"""
This is the "0-add_integer" module.
This module contains a function to add two numbers and return their sum.
"""


def add_integer(a, b):
    """Return the sum of two numbers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
