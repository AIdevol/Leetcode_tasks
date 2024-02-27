class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                
                # Count live neighbors
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and abs(board[x][y]) == 1:
                        live_neighbors += 1
                
                # Apply rules
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Cell dies due to under-population or over-population
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2   # Cell becomes alive due to reproduction
        
        # Update the board
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1   # Alive
                else:
                    board[i][j] = 0   # Dead
