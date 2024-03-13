import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = collections.defaultdict(int)
        n = len(nums) / 2
        for i in nums:
            result[i] += 1
        for k, v in result.items():
            if v >= n:
                return k
            
        