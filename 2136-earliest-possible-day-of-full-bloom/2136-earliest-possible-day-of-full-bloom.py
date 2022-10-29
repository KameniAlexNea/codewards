class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        t = 0
        res = 0
        for g,p in reversed(sorted(zip(growTime, [-i for i in plantTime]))):
            t += -p
            res = max(res, t+g)
        return res