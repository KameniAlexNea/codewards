import collections

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = {}
        for i, v in enumerate(nums):
            if v in duplicate and (i - duplicate[v]) <= k:
                return True
            else:
                duplicate[v] = i
        return False