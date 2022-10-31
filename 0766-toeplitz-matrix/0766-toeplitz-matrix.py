class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pos = 0
        res = collections.defaultdict(set)
        for line in matrix:
            for i, v in enumerate(line, pos):
                res[i].add(v)
                if len(res[i]) != 1:
                    return False
            pos -= 1
        return True