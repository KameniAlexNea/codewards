class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        res = [[1]*i for i in range(1, numRows+1)]
        for i, line_p in enumerate(res[1:-1], 1):
            res[i+1][1:-1] = [
               k1+k2 for k1,k2 in zip(line_p, line_p[1:])
            ]
        return res