class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        result = ""
        index = -1
        for x in s:
            try:
                index = result.index(x)

                best = max(len(result), best)
                result = result[index+1:]+x
            except:
                result += x
        return max(len(result), best)