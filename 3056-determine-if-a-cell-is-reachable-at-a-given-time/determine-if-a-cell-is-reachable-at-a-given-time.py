class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if fx == sx and fy == sy:
            return t != 1
        return max(abs(fx - sx), abs(fy - sy)) <= t
        # compute minimum time to move from (sx, sy) -> (fx, fy)

        diag = min(abs(fx - sx), abs(fy - sy))
        vert = max(abs(fx - sx), abs(fy - sy)) - diag