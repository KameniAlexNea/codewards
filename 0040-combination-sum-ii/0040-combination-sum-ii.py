def _combinationSum2(candidates: list[int], target):
    if len(candidates) == 1:
        return [candidates[0] if candidates[0] == target else None]
    candidates = [i for i in candidates if i <= target]
    if not len(candidates):
        return [None]
    results = [
        [
            i, combinationSum2(candidates[pos+1:], target - i)
        ] for pos, i in enumerate(candidates[:-1])
    ]
    if candidates[-1] == target:
        results += [[target]]
    return results

def combinationSum2(candidates: list[int], target):
    def backtrack(pos, current: list, remaining):
        if remaining == 0:
            valid_combinations.append(current.copy())
            return

        for i in range(pos, len(candidates)):
            if candidates[i] > remaining:
                break
            # Skip duplicates
            if i > pos and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()

    candidates.sort()  # Ensure unique combinations
    valid_combinations = []
    backtrack(0, [], target)
    return valid_combinations

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        return combinationSum2(candidates, target)