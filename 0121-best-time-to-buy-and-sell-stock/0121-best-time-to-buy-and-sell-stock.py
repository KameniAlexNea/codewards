class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min_sell = 1000000
        res = 0
        for price in prices:
            if price-current_min_sell >= res:
                res = price-current_min_sell
            if price < current_min_sell:
                current_min_sell = price
        return res