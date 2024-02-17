import re

def clamp(i):
    min_value = -2**31
    max_value = 2**31 - 1
    return max(min_value, min(max_value, i))

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = re.match(r"^[-+]?\d+", s)
        if res:
            res = res.group()
            return clamp(int(res))
        return 0