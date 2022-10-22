class Solution:
    def numDecodings(self, s: str) -> int:
        computed = {}
        def numDecodingsRec(x):
            if len(x) == 0:
                return 1
            if x[0] == '0':
                return 0
            if len(x) < 3:
                if x[-1] == '0':
                    return 1 if int(x) < 27 else 0
                return 2 if (int(x) < 27 and len(x) == 2) else 1
            l = 0
            if x[1:] not in computed:
                l = numDecodingsRec(x[1:])
            else:
                l = computed[x[1:]]
            if x[2:] not in computed:
                if int(x[:2]) < 27:
                    l += numDecodingsRec(x[2:])
            else:
                if int(x[:2]) < 27:
                    l += computed[x[2:]]
            computed[x] = l
            return l
        return numDecodingsRec(s)