class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            i = nums[0]
            return 1 if i != 1 else 2
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n+1