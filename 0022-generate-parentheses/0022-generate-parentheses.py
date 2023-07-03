def _generateParenthesis(n):
    result = []
    
    def backtrack(cur, open, close, n):
        if open == n and close == n:
            result.append(cur)
            return
        
        if open < n:
            backtrack(cur + '(', open + 1, close, n)
        
        if close < open:
            backtrack(cur + ')', open, close + 1, n)
    
    backtrack('', 0, 0, n)
    return result

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return _generateParenthesis(n)