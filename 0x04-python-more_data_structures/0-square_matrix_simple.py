#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    """
    A function that returns and compute 
    the square value of every integer in a matrix
    """
    newMatrix = []

        for col in matrix:
            result = list(map(lambda x: x**2, col))
            newMatrix.append(result)
        return newMatrix
    
