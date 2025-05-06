class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        return (fx == sx and fy == sy and t != 1) or (
            (fx != sx or fy != sy) and
            (max(abs(fx - sx), abs(fy - sy)) <= t)
        )