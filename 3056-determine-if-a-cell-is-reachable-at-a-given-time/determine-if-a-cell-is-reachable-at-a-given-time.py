class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if fx == sx and fy == sy:
            return t != 1
        return max(abs(fx - sx), abs(fy - sy)) <= t