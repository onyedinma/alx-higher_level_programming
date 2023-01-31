#!/usr/bin/python3
"""Divides elements in a matrix"""


def matrix_divided(matrix, div):
    """divides all elements in a matrix
        r - row
        e- element
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(e, int) or isinstance(e, float))
                    for e in [num for r in matrix for num in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), r)) for r in matrix])
