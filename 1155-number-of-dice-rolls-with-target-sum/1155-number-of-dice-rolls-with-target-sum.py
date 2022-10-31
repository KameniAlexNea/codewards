class Solution:
    def numRollsToTargetRec(self, n, k, t, d: dict):
        # print("Debug: ", n, k, t, d)
        if n == 1:
            return 1
        if t > n*k:
            return 0
        
        v = d.get((n,k,t), None)
        if v is None:
            v = sum(
                self.numRollsToTargetRec(n-1, k, t-i, d) for i in range(max(1, t-(n - 1)*k), 1+min(k, t-(n-1)))
            )
            d[(n,k,t)] = v
        return v
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n*k:
            return 0
        d = {}
        return self.numRollsToTargetRec(n, k, target, d) % (10**9+7)