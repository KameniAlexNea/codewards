class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ls = len(s)
        if ls != len(goal):
            return False
        i = 0
        l = ["", ""]
        h = ["", ""]
        for s1, s2 in zip(s, goal):
            if s1 != s2:
                if i == 2:
                    return False
                l[i] = s1
                h[(i+1) % 2] = s2
                i += 1
        return  (i == 2 and l==h) or (i == 0 and len(set(s)) != ls)