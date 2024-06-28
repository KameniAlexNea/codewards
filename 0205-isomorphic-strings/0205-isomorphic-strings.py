class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mij = dict()
        mji = dict()
        for i, j in zip(s, t):
            if j not in mji and i not in mij:
                mij[i] = j
                mji[j] = i
            if mij.get(i) != j or mji.get(j) != i:
                return False
        return True