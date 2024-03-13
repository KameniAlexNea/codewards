class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        if n == 0:
            return True
        if size == 0:
            return n == 0
        if size == 1:
            return flowerbed[0] == 0 and n <= 1
        i = 0
        while i < size and n > 0:
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == size - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        i += 1  # skip next position
            i += 1
        return n == 0