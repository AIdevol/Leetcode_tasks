class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        
        def get_coordinates(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 1:  # Boustrophedon style
                col = n - 1 - col
            row = n - 1 - row  # Adjusting row to start from the bottom
            return row, col
        
        visited = set()
        queue = deque([(1, 0)])  # (square, moves)
        
        while queue:
            square, moves = queue.popleft()
            if square == target:
                return moves
            
            if square in visited:
                continue
            
            visited.add(square)
            
            for next_square in range(square + 1, min(square + 7, target + 1)):
                next_row, next_col = get_coordinates(next_square)
                if board[next_row][next_col] != -1:
                    next_square = board[next_row][next_col]
                if next_square not in visited:
                    queue.append((next_square, moves + 1))
        
        return -1