class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if not n:
            return True
        if not len(flowerbed) and n:
            return False
        if len(flowerbed) == 1:
            return not flowerbed[0] and n == 1
        if (not flowerbed[0]) and len(flowerbed) > 1 and (not flowerbed[1]):
            flowerbed[0] = 1
            n -= 1
        if (not flowerbed[-1]) and len(flowerbed) > 1 and (not flowerbed[-2]):
            flowerbed[-1] = 1
            n -= 1
        for pos, val in enumerate(zip(flowerbed, flowerbed[1:], flowerbed[2:]), start=1):
            flag = not any(val)
            flowerbed[pos] = int(flag) or val[1]
            n -= flag
            if n == 0:
                return True
        return n < 1