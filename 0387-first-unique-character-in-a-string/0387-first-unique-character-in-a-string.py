class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i in s:
            res[i] = res.get(i, 0) + 1
        for i, v in enumerate(s):
            if res[v] == 1:
                return i
        return -1