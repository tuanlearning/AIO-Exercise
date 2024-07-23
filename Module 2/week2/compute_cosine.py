import numpy as np
import math


def compute_cosine(v1, v2):
    dot_product = sum([v1*v2 for v1, v2 in zip(v1, v2)])
    len_v1 = math.sqrt(sum([x**2 for x in v1]))
    len_v2 = math.sqrt(sum([x**2 for x in v2]))
    result = dot_product / (len_v1*len_v2)
    return result
