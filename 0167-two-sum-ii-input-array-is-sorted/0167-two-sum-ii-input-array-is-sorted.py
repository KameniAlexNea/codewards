class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2 or (len(numbers) == 2 and sum(numbers) != target):
            return []
        if len(numbers) == 2:
            return [1, 2]
        start = 0
        end = len(numbers) - 1
        total = 0
        while start < end:
            total = numbers[start] + numbers[end]
            if total == target:
                return [start + 1, end + 1]
            if total < target:
                start += 1
            else:
                end -= 1
        return []