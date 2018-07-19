#!/usr/bin/env python

import copy

"""
Maximum size square sub-matrix with all 1s
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
For example, consider the below binary matrix.
 --- --- --- --- ---
| 0 | 1 | 1 | 0 | 1 |
 --- --- --- --- ---
| 1 | 1 | 0 | 1 | 0 |
 --- --- --- --- ---
| 0 | 1 | 1 | 1 | 0 |
 --- --- --- --- ---
| 1 | 1 | 1 | 1 | 0 |
 --- --- --- --- ---
| 1 | 1 | 1 | 1 | 1 |
 --- --- --- --- ---
| 0 | 0 | 0 | 0 | 0 |
 --- --- --- --- ---
"""

def max_sub_square(matric_S):
    """
    Algorithm:
        Let the given binary matrix be M[R][C].
        The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j]
        represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost
        and bottommost entry in sub-matrix.
    """
    cols = len(matric_S[0])
    rows = len(matric_S)
    i, j = 0, 0
    init_row = [ 0 for _ in range(cols)]
    # Notice: deepcopy is neccessary
    matric_D = [copy.deepcopy(init_row) for _ in range(rows)]
    while i < cols:
        matric_D[0][i] = matric_S[0][i]
        i += 1

    while j < rows:
        matric_D[j][0] = matric_S[j][0]
        j += 1

    for i in range(1, rows):
        for j in range(1, cols):
            if matric_S[i][j] == 1:
                matric_D[i][j] = min(matric_D[i-1][j], matric_D[i-1][j-1], matric_D[i][j-1]) + 1

    max_square = matric_D[0][0]
    col = 0
    row = 0

    for i in range(rows):
        for j in range(cols):
            if matric_D[i][j] > max_square:
                max_square = matric_D[i][j]
                col = j
                row = i
    return row, col, max_square

if __name__ == "__main__":
    matric_test = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    print max_sub_square(matric_test)
