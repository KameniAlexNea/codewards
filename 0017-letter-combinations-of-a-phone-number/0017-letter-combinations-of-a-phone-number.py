def combine_gpt(digits: str):
    if not digits:
        return []

    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    result = []

    def generate_combinations(combination, remaining_digits):
        if not remaining_digits:
            result.append(combination)
        else:
            for letter in mapping[remaining_digits[0]]:
                generate_combinations(combination + letter, remaining_digits[1:])

    generate_combinations('', digits)
    return result

def combine_alex(digits: str):
    solution = []
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
    def combiner(self, nbers: str, data: str):
        if len(nbers) == 0:
            return solution.append(data)
        for i in letters[nbers[0]]:
            combiner(nbers[1:], data+i)
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(letters[digits], solution)
    combiner(digits, "")
    return solution

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = set(combine_gpt(digits))
        return result