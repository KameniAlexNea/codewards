
def compute(l, r, i):
    if i == "+":
        return int(l) + int(r)
    if i == "-":
        return int(l) - int(r)
    if i == "*":
        return int(l) * int(r)
    return int(int(l) / int(r))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = "+-*/"

        stack = []
        for i in tokens:
            if i not in signs:
                stack.append(i)
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(str(compute(l, r, i)))
        return int(stack[0])