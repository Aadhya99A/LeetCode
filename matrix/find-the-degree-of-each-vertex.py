import numpy as np
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        k = np.array([0]*len(matrix))
        for i in range(len(matrix)):
            k += np.array(matrix[i])
        return k.tolist()