class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        @cache
        def isisInterleaveRec(i, j):
            if i == len(s1) and j == len(s2):
                return True
            res = False
            if i < len(s1) and s3[i+j] == s1[i]:
                res = isisInterleaveRec(i+1, j)
            if not res:
                if j < len(s2) and s3[i+j] == s2[j]:
                    res = isisInterleaveRec(i, j+1)
            return res
        return isisInterleaveRec(0, 0)