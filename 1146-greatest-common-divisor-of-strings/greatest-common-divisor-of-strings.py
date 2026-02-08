def check_divisor(div, w1, w2):
    return (div*(len(w1) // len(div)) == w1) and (div*(len(w2) // len(div)) == w2)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        n1 = len(str1)
        n2 = len(str2)
        result = ""
        
        if str1[0] != str2[0]:
            return ""
        curr = str1[0]
        s = str1[0]
        for a, b in zip(str1[1:], str2[1:]):
            if a != b:
                return ""
            if a == s:
                if (n1%len(curr)==0) and (n2%len(curr) == 0):
                    if check_divisor(curr, str1, str2):
                        result = curr
            curr += a
        if check_divisor(curr, str1, str2):
            result = curr
        return result
