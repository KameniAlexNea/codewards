import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        heapq.heapify(results)
        for i, point in enumerate(points):
            if i < k:
                heapq.heappush(results, (-point[0] ** 2 - point[1]**2, point))
            else:
                heapq.heappushpop(results, (-point[0] ** 2 - point[1]**2, point))
        return [j for _, j in results]