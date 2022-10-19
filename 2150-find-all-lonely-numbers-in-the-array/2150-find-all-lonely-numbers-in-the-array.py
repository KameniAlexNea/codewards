import collections

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        result = collections.defaultdict(int)
        for i in nums:
            result[i] += 1
        return [
            i for i,j in result.items() if (j == 1) and not (((i-1) in result) or ((i+1) in result))
        ]
        