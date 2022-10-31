class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pos = 0
        res = collections.defaultdict(set)
        for line in matrix:
            for i, v in enumerate(line, pos):
                res[i].add(v)
            pos -= 1
        return all(len(v)==1 for v in res.values())