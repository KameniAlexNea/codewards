class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        mat = np.array(mat)
        if prod(mat.shape) == r*c: 
            return np.array(mat).reshape(r, c).tolist()
        else:
            return mat.tolist()
        