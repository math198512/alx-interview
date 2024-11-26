#!/usr/bin/python3
"""
Module for rotating a 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def row_reverse(row):
        """reverse a single row"""
        # Reverse each row manually
        left, right = 0, n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
    for i in range(n):
        row_reverse(matrix[i])
