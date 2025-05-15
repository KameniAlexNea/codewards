from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        indexes = defaultdict(list)
        for i, v in enumerate(nums):
            indexes[v].append(i)
        self.indexes = indexes

    def pick(self, target: int) -> int:
        return random.choice(self.indexes[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)