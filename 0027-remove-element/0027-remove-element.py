class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        pos = 0
        n = len(nums)
        for i, v in enumerate(nums):
            nums[pos] = v
            if v != val:
                pos += 1
        return pos