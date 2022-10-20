class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=r=c=0
        for v in s:
            if v == '(':
                l+=1
            else:
                r+=1
            if l==r:
                c=max(c,l+r)
            elif l < r:
                l = r = 0
        l=r=0
        for v in s[::-1]:
            if v == '(':
                l += 1
            else:
                r += 1
            if l == r:
                c = max(c, l+r)
            elif l > r:
                l = r = 0
        return c
                
        