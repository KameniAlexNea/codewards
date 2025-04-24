def get_state(i, target, results, m, mn, accepted: set):
	to_add = []
	for raw in results:
		if (target > 0 and raw[0] + i > target) or (
			target < 0 and raw[0] + i > 0
		):
			continue
		v = raw + [i]
		v[0] += i
		if len(v) == 5 and v[0] == target:
			accepted.add(tuple(v[1:]))
		elif len(v) < 5:
			if (
				not (
					(target > 0 and v[0] > target) or (target < 0 and v[0] > 0)
				)
			) and (
				(target >= 0 and v[0] + m * (5 - len(v)) >= target)
				or (target < 0 and v[0] + mn * (5 - len(v)) <= target)
			):
				to_add.append(v)
	v = [i, i]
	if (target >= 0 and v[0] + m * (5 - len(v)) >= target) or (target < 0 and v[0] + mn * (5 - len(v)) <= target):
		to_add.append(v)
	return to_add

class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		if len(nums) < 4:
			return []
		if len(nums) == 4:
			if sum(nums) == target:
				return [nums]
			return []
		counts = Counter(nums)

		m = max(counts)
		mn = min(counts)
		if m < target // 4 or mn > target // 4:
			return []
		nums = sorted(counts)
		results = deque([])
		accepted = set()
		for i in nums:
			i_count = counts[i]
			to_add = get_state(i, target, results, m, mn, accepted)
			for j in range(1, i_count):
				results.extend(to_add)
				res_c = to_add
				to_add = get_state(i, target, res_c, m, mn, accepted)
			results.extend(to_add)
		return list(accepted)