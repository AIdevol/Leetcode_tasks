def pivot_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # On a row, if it's begin (left) with a 1 it will always be greater
        # than is it start with a 0

        # On a column, we need to get as many 1 as possible
        x_range = range(len(grid[0]))
        y_len = len(grid)
        y_range = range(y_len)
        
        # While we iterate over the first grid
        # We pivot the matrix
        pivot = [[] for _ in x_range]

        for i in y_range:
            if not grid[i][0]:
                # If the row begin with a 0
                # Flip the line
                for j in x_range:
                    pivot[j].append((grid[i][j]+1)%2)
            else:
                for j in x_range:
                    pivot[j].append(grid[i][j])

        y_2 = y_len/2
        for i in x_range:
            # If we have more 0 than 1
            if sum(pivot[i]) < y_2:
                for j in y_range:
                    grid[j][i] = str((pivot[i][j]+1)%2)
            else:
                for j in y_range:
                    grid[j][i] = str(pivot[i][j])

        # Return the sum of binaries values (1 par line)
        return sum([int(''.join(line), 2) for line in grid])