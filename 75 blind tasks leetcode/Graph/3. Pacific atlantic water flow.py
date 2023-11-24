from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        def dfs(row, col, reachable):
            # Mark the current cell as reachable
            reachable[row][col] = True
            
            # Explore neighbors
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and not reachable[new_row][new_col] and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, reachable)
        
        # DFS from top and bottom borders
        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)
        
        # DFS from left and right borders
        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m - 1, j, atlantic_reachable)
        
        # Find the intersection of cells that can reach both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result