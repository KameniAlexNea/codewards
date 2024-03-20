class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        mapper = {}
        c = 0
        for i in nums:
            if i > k:
                continue
            if mapper.get(i, 0):
                mapper[i] -= 1
                c += 1
            else:
                mapper[k-i] = mapper.get(k-i, 0) + 1
        return c