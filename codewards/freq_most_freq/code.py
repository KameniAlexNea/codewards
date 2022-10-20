from collections import Counter
from functools import cache
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n_counts = dict(Counter(nums))
        unique_n = list(n_counts.keys())
        unique_n.sort()
        maxFreq = 1
        
        @cache
        def compute_count(pos, i):
            count = n_counts[i]
            r = k
            for j in unique_n[:pos][::-1]:
                if r < (i-j):
                    return count
                n_mov = min(r // (i - j), n_counts[j])
                r -= n_mov * (i - j)
                count += n_mov
            return count
        
        for pos, i in enumerate(unique_n):
            maxFreq = max(maxFreq, compute_count(pos, i))
        return maxFreq