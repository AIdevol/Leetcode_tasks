class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    current = board[i][j]
                    # Check for rows
                    if (i, current) in seen:
                        return False
                    seen.add((i, current))
                    
                    # Check for columns
                    if (current, j) in seen:
                        return False
                    seen.add((current, j))
                    
                    # Check for sub-boxes
                    if (i // 3, j // 3, current) in seen:
                        return False
                    seen.add((i // 3, j // 3, current))

        return True
