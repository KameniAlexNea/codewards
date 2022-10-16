class Solution:
    def partitionString(self, s: str) -> int:
        partition = set()
        c = 1
        for i in s:
            if i not in partition:
                partition.add(i)
            else:
                partition = {i}
                c += 1
        return c
        