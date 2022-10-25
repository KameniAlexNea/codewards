import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n == r*c:
            return np.array(mat).reshape(r, c).tolist()
        else:
            return mat
        