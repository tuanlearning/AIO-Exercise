import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    result = np.linalg.eig(matrix)
    return result[0], result[1]


matrix = np.array([[-6, 3], [4, 5]])
