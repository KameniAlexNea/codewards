class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, v1 in enumerate(nums):
            if result.get(target - v1) is None:
                result[v1] = i
            else:
                return [result[target - v1], i]