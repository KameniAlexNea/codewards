class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currsum = 0
        for i in nums:
            if(currsum < 0):
                currsum=0
            currsum += i
            res = max(res, currsum)
        return res