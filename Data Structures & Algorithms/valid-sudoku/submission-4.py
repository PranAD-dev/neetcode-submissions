class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(list)
        cols = defaultdict(list)
        sqrs = defaultdict(list)

        for i in range(n):
            for j in range(n):
                key = (i//3, j//3)
                current = board[i][j]
                if current != ".":
                    if current in rows[i] or current in cols[j] or current in sqrs[key]:
                        return False
                
                rows[i].append(current)
                cols[j].append(current)
                sqrs[key].append(current)

        return True