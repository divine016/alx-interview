#!/usr/bin/python3
"""
A funnumtion to print the pascal triangle.
def pascal_triangle(n): 
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): 
    prints the of  Pascal’s triangle of n 
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            arr = []
            num = 1
            for j in range(1, i + 1):
                arr.append(num)
                num = num * (i - j) // j
            triangle.append(arr)
    return triangle