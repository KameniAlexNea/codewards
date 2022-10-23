from collections import defaultdict
from itertools import chain

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d_nums1 = defaultdict(int)
        for i in nums1:
            d_nums1[i] += 1
        d_nums2 = defaultdict(int)
        for i in nums2:
            d_nums2[i] += 1
        if len(d_nums2) < len(d_nums1):
            d_nums1, d_nums2 = d_nums2, d_nums1
        res = chain(
            *[[i]*min(j, d_nums2.get(i, 0)) for i, j in d_nums1.items()]
        )
        return res