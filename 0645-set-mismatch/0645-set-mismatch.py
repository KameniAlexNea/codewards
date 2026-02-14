class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        r = [0, 0]
        raw = [0] * len(nums)
        for i in nums:
            raw[i-1] += 1
        c = 0
        for i, j in enumerate(raw):
            if j == 2:
                r[0] = i + 1
                c += 1
            if j == 0:
                r[1] = i + 1
                c += 1
            if c == 2:
                return r
