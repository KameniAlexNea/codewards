class Solution:
    def intToRoman(self, num: int) -> str:
        m = num // 1000
        res = ""
        if m > 0:
            res += "M" * m
            num -= m * 1000
        if num >= 900:
            res += "CM"
            num -= 900
        elif num >= 500:
            res += "D"
            num -= 500
        elif num >= 400:
            res += "CD"
            num -= 400
        
        c = num // 100
        if c > 0:
            res += "C" * c
            num -= c * 100
        if num >= 90:
            res += "XC"
            num -= 90
        elif num >= 50:
            res += "L"
            num -= 50
        elif num >= 40:
            res += "XL"
            num -= 40
            
        x = num // 10
        if x > 0:
            res += "X" * x
            num -= x * 10
        if num >= 9:
            res += "IX"
            num -= 9
        elif num >= 5:
            res += "V"
            num -= 5
        elif num >= 4:
            res += "IV"
            num -= 4
        return res + ("I" * num)