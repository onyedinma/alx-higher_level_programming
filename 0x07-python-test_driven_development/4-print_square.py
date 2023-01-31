#!/usr/bin/python3
"""Prints a square with a '#' character"""


def print_square(size):
    """Prints a square with '#' character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
