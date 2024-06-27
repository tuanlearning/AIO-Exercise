import numpy as np
source = 'def'
target = 'dafabc'


def findLevenshtein(source: str, target: str) -> int:
    matrix = np.zeros((len(source)+1, len(target) + 1))
    # setting the base case for first row
    matrix[0] = [float(i) for i in range(len(matrix[0]))]
    # setting the base case for first column
    matrix[:, 0] = [float(i) for i in range(len(matrix[:, 0]))]
    for i in range(1, len(source)+1):  # i = source
        for j in range(1, len(target) + 1):  # j = target
            if source[i-1] == target[j-1]:
                matrix[i, j] = matrix[i-1, j-1]
            else:
                matrix[i, j] = min(matrix[i-1, j-1] + 1,
                                   matrix[i-1, j] + 1, matrix[i, j-1]+1)
    return int(matrix[-1, -1])
