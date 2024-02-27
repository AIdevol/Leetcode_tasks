class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        x, y, dx, dy = 0, 0, 1, 0
        
        for i in range(m * n):
            res.append(matrix[y][x])
            matrix[y][x] = None
            
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y+dy][x+dx] is None:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        
        return res