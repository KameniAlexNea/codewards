from heapq import merge

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = list(merge(nums1, nums2))
        size = len(result)
        if size == 0:
            return 0
        elif size == 1:
            return result[0]
        if int(size / 2) < (size/2):
            return result[size//2]
        return (result[size//2] + result[size//2 - 1]) / 2