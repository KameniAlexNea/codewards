import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = dict()
        n = len(nums) / 2
        for i in nums:
            result[i] = result.get(i, 0) + 1
        for k, v in result.items():
            if v >= n:
                return k
            
        