class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverse(self, matrix):
        n = len(matrix)
        
        # Reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate(self, matrix):
        # Transpose and then reverse
        self.transpose(matrix
        self.reverse(matrix)
