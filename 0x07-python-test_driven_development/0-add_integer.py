#!/usr/bin/python3
"""
This module defines a function to add two numbers together, input validation.

function add_integer(a, b) takes arguments, a and b, and returns their sum.
If argument is not an integer or float, TypeError is raised. Floats are
cast to integers before addition.
"""


def add_integer(a, b):
    """Returns the numbers sum a and b, after type conversion if necessary."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("Input a must be a number")
    if type(b) is not int and type(b) is not float:
        raise TypeError("Input b must be a number")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
