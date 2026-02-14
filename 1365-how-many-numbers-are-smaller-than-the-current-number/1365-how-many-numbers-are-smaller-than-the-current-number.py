class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        res = {}

        for i, j in enumerate(nums_sorted):
            if j not in res:
                res[j] = i
        return [
            res[i] for i in nums
        ]