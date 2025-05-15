class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # if len(nums) <= 5:
        #    return list(set(nums))
        count1 = 0
        count2 = 0
        count3 = 0
        pos1 = None
        pos2 = None
        pos3 = None
        for i in nums:
            if count1 == 0:
                pos1 = i
            elif count2 == 0:
                pos2 = i
            elif count3 == 0:
                pos3 = i
            if i == pos1:
                count1 += 1
            elif i == pos2:
                count2 += 1
            elif i == pos3:
                count3 += 1
            else:
                count1 -= 1
                count2 -= 1
                count3 -= 1
        count1, count2, count3 = 0, 0, 0
        for i in nums:
            if i == pos1:
                count1 += 1
            elif i == pos2:
                count2 += 1
            elif i == pos3:
                count3 += 1
        count_min = len(nums) // 3
        return [p for p, c in zip([pos1, pos2, pos3], [count1, count2, count3]) if c > count_min]

            