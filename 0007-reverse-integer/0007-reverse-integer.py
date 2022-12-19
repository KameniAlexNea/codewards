class Solution:
    def reverse(self, x: int) -> int:
        base = ""
        pos = 0
        if x < 0:
            pos = 1
            base = "-"
        res = base + str(x)[pos:][::-1]
        res = int(res)
        return res if (-2**31 <= res <= 2**31-1) else 0