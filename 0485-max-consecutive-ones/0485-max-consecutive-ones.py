class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        start = 0
        for i in nums:
            if i == 1:
                start += 1
            else:
                r = max(r, start)
                start = 0
        r = max(r, start)
        return r