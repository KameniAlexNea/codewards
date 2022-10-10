class Solution:
    def isValid(self, s: str) -> bool:
        res = ""
        map_validation = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for x in s:
            if x in map_validation:
                if len(res) <= 0 or res[-1] != map_validation[x]:
                    return False
                else:
                    res = res[:-1]
            else:
                res += x
        return len(res) == 0
        