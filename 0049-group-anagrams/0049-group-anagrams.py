import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i,v in enumerate(strs):
            d["".join(sorted(v))].append(v)
        return [
            v for v in d.values()
        ]