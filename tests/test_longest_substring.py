from codewards.LongestSubstring.code import Solution

def test_case1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test_case2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

def test_case3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3