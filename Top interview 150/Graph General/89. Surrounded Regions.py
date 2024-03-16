class Solution:

    def solve(self, board: List[List[str]]) -> None:
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        m, n = len(board), len(board[0])

        def dfs(i,j,m,n):
            visited.add((i,j))
            for row,col in dir:
                newRow = i + row
                newCol = j + col
                if( newRow >=0 and newRow < m and newCol>=0 
                    and newCol < n and (newRow,newCol) not in visited
                    and board[newRow][newCol] == "O"):
                    dfs(newRow,newCol,m,n)

        # rows
        for i in range(0,n):
        
            # first row
            if(board[0][i] == "O"  and (0,i) not in visited):
                dfs(0,i,m,n)
            # last row
            if(board[m - 1][i] == "O"  and (m-1,i) not in visited):
                dfs(m-1,i,m,n)
        # cols
        for j in range(0,m):
             # first col
            if(board[j][0] == "O" and (j,0) not in visited):
                dfs(j,0,m,n)
            # last col
            if(board[j][n - 1] == "O"  and (j,n-1) not in visited):
                dfs(j,n-1,m,n)
        
        for i in range(m):
            for j in range(n):
                if(board[i][j] == "O" and (i,j) not in visited):
                    board[i][j] = "X"
        """
        Do not return anything, modify board in-place instead.
        """