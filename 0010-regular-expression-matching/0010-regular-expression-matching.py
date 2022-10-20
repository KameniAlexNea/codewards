class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        res = re.match(p, s)
        return (res is not None) and (res.group() == s)