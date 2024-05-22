#!/usr/bin/python3
"""function that returns a list of
integers representing the Pascal's triangle of n:"""


def pascal_triangle(n):
    """technical interview prep"""
    if n <= 0:
        return []

    pt = [[1]]
    while len(pt) != n:
        triangle = pt[-1]
        hold = [1]
        for o in range(len(triangle) - 1):
            hold.append(triangle[o] + triangle[o + 1])
        hold.append(1)
        pt.append(hold)
    return pt
