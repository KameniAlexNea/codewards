from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = {}
        for i in nums:
            res[i] = 1
        r = []
        for i in range(len(nums)):
            if not res.get(i+1, 0):
                r.append(i + 1)
        return r