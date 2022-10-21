import collections
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicateBruteForce(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def checkBrute(values, i) -> bool:
            return any((abs(i-j) <= valueDiff) for j in values)
        
        duplicate = {}
        for i, u in enumerate(nums[:indexDiff]):
            for v in nums[:indexDiff][i+1:]:
                if abs(v-u) <= valueDiff:
                    return True
        for i, u in enumerate(nums[indexDiff:], indexDiff):
            if checkBrute(nums[(i-indexDiff):i], u):
                return True
        return False
    
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        leng = len(nums)
        for idx, n in enumerate(nums):
		    # remove the element whose index is invalid
            if idx > indexDiff:
                window.remove(nums[idx-indexDiff-1])
			# add current element to sliding window
            window.add(n)
			# find the first location of current element
            leftbound = window.bisect_left(n)
			# check if its right and left side element meet the problem requirement.
            if leftbound > 0 and abs(window[leftbound] - window[leftbound-1]) <= valueDiff:
                return True
            if leftbound < len(window)-1 and abs(window[leftbound+1] - window[leftbound]) <= valueDiff:
                return True
        return False