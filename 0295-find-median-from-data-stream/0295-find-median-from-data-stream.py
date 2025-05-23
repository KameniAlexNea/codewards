import heapq

class MedianFinder:

    def __init__(self):
        self.low = []  # max-heap (invert values)
        self.high = [] # min-heap
        heapq.heapify(self.low)
        heapq.heapify(self.high)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # Maintain size property: len(low) ≥ len(high)
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()