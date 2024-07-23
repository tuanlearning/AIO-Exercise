import numpy as np
import math


def matrix_multi_matrix(matrix1, matrix2):
    return matrix1.dot(matrix2)


matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix_multi_matrix(matrix1, matrix2)
