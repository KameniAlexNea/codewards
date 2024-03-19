import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        regex = ".*" + (".*".join(list(s))) + ".*"
        return re.match(regex, t) is not None