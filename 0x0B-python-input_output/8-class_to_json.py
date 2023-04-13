#!/usr/bin/python3
""" A module that provides a function to generate a dictionary-based
description using a basic data structure for serializing an object in JSON format
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
