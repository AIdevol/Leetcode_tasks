class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board, word, i, j, k, visited):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[k]:
                return False
            
            visited[i][j] = True
            if backtrack(board, word, i + 1, j, k + 1, visited) \
                    or backtrack(board, word, i - 1, j, k + 1, visited) \
                    or backtrack(board, word, i, j + 1, k + 1, visited) \
                    or backtrack(board, word, i, j - 1, k + 1, visited):
                return True

            visited[i][j] = False
            return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, word, i, j, 0, visited):
                    return True
        return False
