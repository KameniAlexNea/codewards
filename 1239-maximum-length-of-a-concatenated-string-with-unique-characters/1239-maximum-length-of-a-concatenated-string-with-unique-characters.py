class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [
            set(i) for i in arr if len(set(i)) == len(i)
        ]
        if len(arr) == 0:
            return 0
        res = [set()]
        for i in arr:
            for c in res:
                if len(i.intersection(c)) == 0:
                    res.append(c.union(i))
        return max(len(v) for v in res)
        