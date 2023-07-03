class Solution:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def combiner(self, nbers: str, data: str, solution: list):
        if len(nbers) == 0:
            return solution.append(data)
        for i in self.letters[nbers[0]]:
            self.combiner(nbers[1:], data+i, solution)
    
    def letterCombinations(self, digits: str) -> list[str]:
        solution = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.letters[digits])
        self.combiner(digits, "", solution)
        result = set(solution)
        return result