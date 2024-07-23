import numpy as np
import math


def compute_vector_length(vector):
    return math.sqrt(sum([x**2 for x in vector]))


def compute_vector_length(vector):
    return np.linalg.norm(vector)


vector = np.array([1, 2, 3, 4])
compute_vector_length(vector)
