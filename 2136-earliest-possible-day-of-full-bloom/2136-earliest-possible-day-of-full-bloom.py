class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        argSorted = sorted(range(len(plantTime)), key=lambda x: (-growTime[x], plantTime[x]))
        plantEndTime = {}
        p = 0
        res = 0
        for i in argSorted:
            p += plantTime[i]
            res = max(res, p+growTime[i])
        return res