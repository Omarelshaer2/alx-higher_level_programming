#!/usr/bin/python3
"""
The lookup function allows searching for data
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
