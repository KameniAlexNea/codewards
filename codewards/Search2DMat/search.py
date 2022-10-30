from typing import List


class Solution:
    def searchListRec(self, line: List[int], left, right, target):
        if right <= left+1:
            return (line[left] == target) or (line[right] == target)
        mid = (left + right) // 2
        elm = line[mid]
        if elm == target:
            return True
        elif elm < target:
            return self.searchListRec(line, mid, right, target)
        return self.searchListRec(line, left, mid, target)
        
        
    def searchMatrixRec(self, matrix: List[List[int]], left, right, target):
        if right <= left+1:
            line = matrix[right]
            if line[0] == target:
                return True
            elif line[0] < target:
                return self.searchListRec(line, 0, len(line) - 1, target)
            line = matrix[left]
            return self.searchListRec(line, 0, len(line) - 1, target)
        
        mid = (left + right) // 2
        elm = matrix[mid][0]
        
        if elm == target:
            return True
        elif elm < target:
            return self.searchMatrixRec(matrix, mid, right, target)
        return self.searchMatrixRec(matrix, left, mid, target)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixRec(matrix, 0, len(matrix)-1, target)