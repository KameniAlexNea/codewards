class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t_dict = {}
        for i in magazine:
            t_dict[i] = t_dict.get(i, 0) + 1
        
        for i in ransomNote:
            t_dict[i] = t_dict.get(i, 0) - 1
            if t_dict[i] < 0:
                return False
        return True