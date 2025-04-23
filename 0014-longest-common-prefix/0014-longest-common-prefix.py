class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or any(not i for i in strs):
            return ""
        if len(strs) == 1:
            return strs[0]
        result = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            result += i[0]
        return result