class Solution:
    def makeGood(self, s: str) -> str:
        p = False
        i = 0
        while i < len(s)-1:
            if (s[i].lower() == s[i+1].lower()) and ((s[i].islower() and s[i+1].isupper()) or (s[i+1].islower() and s[i].isupper())):
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i = i + 1
        return s