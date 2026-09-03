class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)
        
        for i in range(length):
            for j in range(len(board[i])):
                val = board[i][j]
                key = (i//3, j//3)
                if val != "." and (val in rows[i] or val in cols[j] or val in grids[key]):
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grids[key].add(val)
        
        return True
                
