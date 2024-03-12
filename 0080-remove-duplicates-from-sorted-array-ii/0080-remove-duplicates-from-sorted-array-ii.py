class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = nums[0]
        count = 1
        
        i = 0
        for v in nums[1:]:
            if v == curr:
                count += 1
                if count < 3:
                    i += 1
                nums[i] = v
            else:
                curr = v
                count = 1
                i += 1
                nums[i] = v
        return i+1