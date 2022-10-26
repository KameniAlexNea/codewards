class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
            ( s + (n * k)) % k <==> (s % k)
        """
        dc = {0: -1}
        s = 0
        for i, v in enumerate(nums):
            s = (s + v) % k
            if s not in dc:
                dc[s] = i
            else:
                if i - dc[s] >= 2:
                    return True
        return False