#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """for a 2 by 2 matrix
    
    Keyword arguments:
    matrix -- A 2 array
    Return: squar 2 array
    """
    
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
    return squared

