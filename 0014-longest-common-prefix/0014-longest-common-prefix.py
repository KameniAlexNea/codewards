class Solution:
    def get_prefix(self, a, b):
        s = ""
        pos = 0
        n = min(len(a), len(b))
        while pos < n and a[pos] == b[pos]:
            s += a[pos]
            pos += 1
        return s
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or any(len(s)==0 for s in strs):
            return ""
        if len(strs) == 1:
            return strs[0]
        res = self.get_prefix(strs[0], strs[1])
        pos = 2
        while pos < len(strs) and res != "":
            res = self.get_prefix(res, strs[pos])
            pos += 1
        return res