class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
    def majorityElementI(self, nums: list[int]) -> int:
        result = dict()
        n = len(nums) / 2
        for i in nums:
            result[i] = result.get(i, 0) + 1
        for k, v in result.items():
            if v >= n:
                return k
            
        