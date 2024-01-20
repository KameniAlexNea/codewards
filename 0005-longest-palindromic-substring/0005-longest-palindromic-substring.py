def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longest_palindromic_substring(s):
    start = 0
    end = 0
    
    for i in range(len(s)):
        left1, right1 = expand_around_center(s, i, i)  # Odd length palindrome
        left2, right2 = expand_around_center(s, i, i + 1)  # Even length palindrome
        
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    
    return s[start:end + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindromic_substring(s)