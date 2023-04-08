#!/usr/bin/python3
"""
This module defines a function, matrix_divided(matrix, div),
which divides all elements of the input matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """Divides all elements of the matrix by the given divisor."""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for Lox in matrix:
        if type(Lox) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(Lox)
        elif size != len(Lox):
            raise TypeError("Each row of the matrix must have the same size")
        for i in Lox:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in Lox] for Lox in matrix]
