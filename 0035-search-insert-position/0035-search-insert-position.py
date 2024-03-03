class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        while pos < len(nums) and nums[pos] < target:
            pos += 1
        return pos
        if pos == len(nums):
            return pos
        
        