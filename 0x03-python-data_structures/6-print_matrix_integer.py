#!/usr/bin/python3
# 6-print_matrix_integer.py
# Brennan D Baraban <375@holbertonschool.com>


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(col) for col in row))
