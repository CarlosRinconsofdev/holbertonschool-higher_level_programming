#!/usr/bin/python3
"""
matrix_divided:
Write a function that divides all elements of a matrix.
"""


from operator import ne
import re
from typing import TYPE_CHECKING


def matrix_divided(matrix, div):
    """
    Div all elements of a matrix

    Args:
        matrix (list of lists): lists of int or float
        div (int or float): must be a number

    Raise:
        TypeError: exception with the message div must be a number.
        ZeroDivisionError: exception with the message division by zero.

    Return:
        a new matrix.
    """
    if type(div) not in [int, float] or div != div or\
            abs(div) > 1.7976931348623158e+308:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    if type(matrix) is list:
        new_matrix = [x[:] for x in matrix]
        for i in range(len(matrix)):
            if i <= len(matrix) - 2 and len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same" +
                                " size")
                return matrix
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float] or\
                        matrix[i][j] != matrix[i][j] or\
                        abs(matrix[i][j]) > 1.7976931348623158e+308:
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    " of integers/floats")
                    return matrix
                else:
                    new_matrix[i][j] = round(matrix[i][j] / div, 2)
    else:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
        return matrix

    return new_matrix