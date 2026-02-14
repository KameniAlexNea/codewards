class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [
            [i, j] for i, j in zip(nums, nums[n:])
        ]
        return sum(result, start=[])