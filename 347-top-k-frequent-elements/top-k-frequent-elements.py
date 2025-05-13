from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list((j, i) for i, j in Counter(nums).items())
        results = []
        heapq.heapify(results)
        for raw, _ in zip(counts, range(k)):
            heapq.heappush(results, raw)
        for raw in counts[k:]:
            heapq.heappushpop(results, raw)
        return [heapq.heappop(results)[1] for _ in range(len(results))]