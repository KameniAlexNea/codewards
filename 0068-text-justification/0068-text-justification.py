def repartir_entier(n, k):
    quotient = n // k
    reste = n % k
    repartition = [quotient] * k
    for i in range(reste):
        repartition[i] += 1
    return repartition

class Solution:
    
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        results = []
        i = 0
        n = len(words)
        while i < n:
            raw = []
            size = 0
            n_words = 0
            while i < n and (size + n_words + len(words[i])) <= maxWidth:
                w = words[i]
                raw.append(w)
                n_words += 1
                size += len(w)
                i += 1
            if i < n:
                repartition = repartir_entier(maxWidth-size, max(n_words-1, 1))
                if len(raw) == 1:
                    raw_w = raw[0] + " " * repartition[0]
                else:
                    raw_w = "".join([
                        v + " " * r for v, r in zip(raw, repartition)
                    ]) + raw[-1]
            else:
                extra_space = (maxWidth-size-n_words+1) 
                raw_w = (" ").join(raw)
                raw_w = raw_w + " " * extra_space

            results.append(raw_w)
        return results