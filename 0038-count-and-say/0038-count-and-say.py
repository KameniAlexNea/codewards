class Solution:
    def sayFunc(self, n) -> str:
        s = str(n)
        result = ""
        prec = s[0]
        count = 1
        for x in s[1:]:
            if x == prec:
                count += 1
            else:
                result += str(count)+str(prec)
                prec = x
                count = 1
        result += str(count)+str(prec)
        return result
    
    def countAndSay(self, n: int):
        if n == 1:
            return "1"
        say = "1"
        for _ in range(1, n):
            say = self.sayFunc(say)
        return say