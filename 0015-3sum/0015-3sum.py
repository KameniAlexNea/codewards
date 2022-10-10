from collections import defaultdict
from itertools import combinations

class Solution:
    def threeSumV1(self, nums: List[int]) -> List[List[int]]:
        d_res = defaultdict(lambda: defaultdict(dict))
        def update_func(x):
            x = sorted(x)
            d_res[x[0]][x[1]][x[2]] = True
            
        results = [
            update_func([x1, x2, x3]) for x1,x2,x3 in combinations(nums,3) if (x1+x2+x3 == 0)
        ]
        return [
            [x1, x2, x3] for x1, v1 in d_res.items() for x2,v2 in v1.items() for x3 in v2.keys()
        ]
    def threeSumV2(self, nums: List[int]) -> List[List[int]]:
        results = set(
            tuple(sorted(l)) for l in combinations(nums,3) if (sum(l) == 0)
        )
        return [
            list(l) for l in results
        ]
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        
        for idx, val in enumerate(nums[:-2]):
            if val>0:
                break
            if val == nums[idx -1] and idx>0:
                continue
            left_point = idx+1
            right_point = len(nums)-1
            
            while left_point<right_point:
                three_sum = nums[left_point]+nums[right_point]+val
                if three_sum == 0:
                    output.append([nums[left_point], nums[right_point], val])
                if three_sum > 0:
                    right_point -=1
                else:
                    left_point +=1
                    while nums[left_point] == nums[left_point-1] and left_point<right_point:
                        left_point +=1
        return output