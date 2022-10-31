class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for r, line in enumerate(board):
            for c, value in enumerate(line):
                if value==".":
                    continue
                # check if current board isin rows, cols or squares
                if (value in rows[r] or value in cols[c] or value in squares[(r//3,c//3)]): 
                    return False
                cols[c].add(value)
                rows[r].add(value)
                squares[(r//3,c//3)].add(value)
        return True