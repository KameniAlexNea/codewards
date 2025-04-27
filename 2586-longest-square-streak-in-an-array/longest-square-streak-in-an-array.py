class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squared = set(i**2 for i in nums)
        longest = 0
        for i in squared:
            if i ** .5 not in squared:
                start = i
                size = 0
                while i in squared:
                    i *= i
                    size += 1
                longest = max(longest, size)
        return longest if longest > 1 else -1