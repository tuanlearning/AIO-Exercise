import numpy as np
import math


def compute_dot_product(v1, v2):
    return sum([v1*v2 for v1, v2 in zip(v1, v2)])


def compute_dot_product(v1, v2):
    return v1.dot(v2)


v1 = np.array([1, 2, 3, 4])
v2 = np.array([2, 3, 4, 5])
compute_dot_product(v1, v2)
