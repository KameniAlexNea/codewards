import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = collections.defaultdict(int)
        for i in words:
            result[i] += 1
        return sorted(list(result.keys()), key=lambda x: (-result[x], x))[:k]