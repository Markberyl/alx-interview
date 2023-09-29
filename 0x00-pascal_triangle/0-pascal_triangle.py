#!/usr/bin/python3
"""
    0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    t_row = [1]
    temp_l = [0]
    Tri = []

    if n <= 0:
        return Tri

    for i in range(n):
        Tri.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return Tri
