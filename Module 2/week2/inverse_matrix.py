import numpy as np


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)


matrix1 = np.array([[1, 2, 0], [4, 5, 6], [7, 8, 9]])

inverse_matrix(matrix1)
