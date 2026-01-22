class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = tuple(sorted(nums))
        n = len(nums)

        diff = 100000000
        total = 100000000
        flag = False
        for i in range(n):
            j = i+1
            k = n - 1
            while j < k :
                vj = nums[j]
                vk = nums[k]
                r = target - nums[i]
                if vj + vk == r:
                    return target
                if abs(vj + vk - r) < diff:
                    total = vj + vk + nums[i]
                    diff = abs(total - target)
                
                while j+1 < k and nums[j+1] == vj:
                    j += 1
                    flag = True
                if flag and abs(vj + vj - r) < diff:
                    total = vj + vj + nums[i]
                    diff = abs(total - target)
                    if diff == 0:
                        return total
                    flag = False
                
                while k-1 > j and nums[k-1] == vk:
                    k -= 1
                    flag = True
                if flag and abs(vk + vk - r) < diff:
                    total = vk + vk + nums[i]
                    diff = abs(total - target)
                    if diff == 0:
                        return total
                    flag = False
                
                if vj + vk > r:
                    k -= 1
                else:
                    j += 1
        return total
            
