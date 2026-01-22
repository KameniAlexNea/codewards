def compute(i, j):
    if i == "0" and j == "0":
        return "0", "0"
    if i == "0" or j == "0":
        return "1", "0"
    return "0", "1"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        a = "0"*(len(b) - len(a)) + a
        r = "0"
        curr = ""
        for i, j in zip(b[::-1], a[::-1]):
            s, r1 = compute(i, j)
            if r != "0":
                s, r2 = compute(s, r)
                r1 = max(r1, r2)
            r = r1
            curr = s + curr
        if r != "0":
            curr = r + curr
        return curr

        