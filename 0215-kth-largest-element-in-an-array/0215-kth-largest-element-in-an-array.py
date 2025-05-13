import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        heapq.heapify(result)
        for i, _ in zip(nums, range(k)):
            heapq.heappush(result, i)
        for i in nums[k:]:
            heapq.heappushpop(result, i)
        return heapq.heappop(result)
        