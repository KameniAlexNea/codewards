/**
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
            ( s + (n * k)) % k <==> (s % k)
        """
        dc = {0: -1}
        s = 0
        for i, v in enumerate(nums):
            s = (s + v) % k
            if s not in dc:
                dc[s] = i
            else:
                if i - dc[s] >= 2:
                    return True
        return False
*/

import java.util.*; 


class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0, -1);
        int s = 0;
        for (int i=0; i < nums.length; i++) {
            s = (s + nums[i]) % k;
            if (map.containsKey(s)) {
                if (i - map.get(s) >= 2) return true;
            } else {
                map.put(s, i);
            }
        }
        return false;
    }
}