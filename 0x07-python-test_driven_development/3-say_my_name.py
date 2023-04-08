#!/usr/bin/python3
"""
This module defines say_my_name function that can used to print a person's name
"""


def say_my_name(first_name, last_name=""):
    """Prints the person's name, given their first name and last name."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
