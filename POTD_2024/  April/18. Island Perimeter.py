class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Each land cell contributes 4 to perimeter
                    # Check adjacent cells
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2  # Subtract 2 if adjacent cell is also land (top)
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2  # Subtract 2 if adjacent cell is also land (left)

        return perimeter