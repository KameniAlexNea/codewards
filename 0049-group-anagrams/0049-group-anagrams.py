import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i,v in enumerate(strs):
            d["".join(sorted(v))].append(i)
        return [
            [strs[i] for i in v] for v in d.values()
        ]