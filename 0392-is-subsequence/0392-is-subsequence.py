import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        regex = ".*".join(list(s))
        return len(re.findall(regex, t)) > 0