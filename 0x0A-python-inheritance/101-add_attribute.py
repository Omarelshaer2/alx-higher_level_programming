#!/usr/bin/python3
""" This function called is_same_class """


def add_attribute(prmObject, prmName, prmValue):
    """ add_attribute function """
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)
