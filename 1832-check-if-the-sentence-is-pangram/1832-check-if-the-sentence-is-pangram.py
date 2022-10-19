class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import re
        sentence = "".join(re.findall("[a-z]*", sentence))
        return len(set(sentence)) == 26