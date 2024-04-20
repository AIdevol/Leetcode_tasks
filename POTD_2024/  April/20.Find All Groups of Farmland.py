class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] != 1:
                return
            land[r][c] = 0
            nonlocal top_left, bottom_right
            top_left = [min(top_left[0], r), min(top_left[1], c)]
            bottom_right = [max(bottom_right[0], r), max(bottom_right[1], c)]
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        m, n = len(land), len(land[0])
        result = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    dfs(i, j)
                    result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        return result