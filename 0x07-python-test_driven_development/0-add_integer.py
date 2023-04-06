#!/usr/bin/python3
"""
This module defines a function to add two numbers together, with input validation.

The function add_integer(a, b) takes two arguments, a and b, and returns their sum.
If either argument is not an integer or a float, a TypeError is raised. Floats are
cast to integers before addition.
"""


def add_integer(a, b):
    """Returns the sum of two numbers a and b, after type conversion if necessary."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("Input a must be a number")
    if type(b) is not int and type(b) is not float:
        raise TypeError("Input b must be a number")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
