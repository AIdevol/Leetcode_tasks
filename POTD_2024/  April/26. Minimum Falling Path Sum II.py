class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        previous_row = grid[0]

        # Process each row starting from the second row
        for i in range(1, n):
            current_row = grid[i]
            new_dp_row = [0] * n
            min1 = float('inf')
            min2 = float('inf')
            min1_index = -1
            
            # Determine the two smallest values and their indices in previous_row
            for j in range(n):
                if previous_row[j] < min1:
                    min2 = min1
                    min1 = previous_row[j]
                    min1_index = j
                elif previous_row[j] < min2:
                    min2 = previous_row[j]

            # Compute DP values for the current row
            for j in range(n):
                if j == min1_index:
                    new_dp_row[j] = current_row[j] + min2
                else:
                    new_dp_row[j] = current_row[j] + min1
            
            # Move to the next row
            previous_row = new_dp_row

        # The result is the minimum value in the last processed row
        return min(previous_row)