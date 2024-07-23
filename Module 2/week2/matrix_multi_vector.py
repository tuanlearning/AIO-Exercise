import numpy as np
import math


def matrix_multi_vector(matrix, vector):
    return matrix.dot(vector)


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 2, 3])

matrix_multi_vector(matrix, vector)
