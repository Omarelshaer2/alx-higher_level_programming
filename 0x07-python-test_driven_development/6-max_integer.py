#!/usr/bin/python3
"""This module defines a function to find the maximum integer in a list of integers."""


def max_integer(list=[]):
    """This function takes a list of integers as input and returns the maximum integer value.
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
