class Solution {
    public int maxProfit(int[] prices) {
        int curr_min = 1000000;
        int res = 0;
        for (int i = 0; i < prices.length; i++) {
            int k = prices[i];
            if (k-curr_min > res) {
                res = k-curr_min;
            }
            if (k < curr_min) {
                curr_min = k;
            }
        }
        return res;
    }
}