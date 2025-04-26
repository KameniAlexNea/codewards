class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for i in unique_nums:
            if i - 1 not in unique_nums:
                start = i
                size = 1

                while start + 1 in unique_nums:
                    start += 1
                    size += 1
                longest = max(longest, size)
        return longest