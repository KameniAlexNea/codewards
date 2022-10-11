class Solution:
    def climbStairsRec(self, n: int):
        if n <= 3:
            return n
        return self.climbStairsRec(n-2) + self.climbStairsRec(n-1)
    
    def climbStairsDynamic(self, n: int):
        if n <= 3:
            return n
        res_list = [0]*n
        res_list[0] = 1
        res_list[1] = 2
        for i in range(2, n):
            res_list[i] = res_list[i-1] + res_list[i-2]
        return res_list[-1]
    
    def climbStairsDynamicLowMem(self, n: int):
        if n <= 3:
            return n
        prec_prec_val = 1
        prec_val = 2
        for i in range(2, n):
            prec_prec_val, prec_val = prec_val, (prec_val + prec_prec_val)
        return prec_val
    
    def climbStairs(self, n: int) -> int:
        return self.climbStairsDynamicLowMem(n)