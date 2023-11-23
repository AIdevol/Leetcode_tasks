class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        half=[1]*n
        for i in range (1,m):
            for j in range(1,n):
                half[j]+=half[j-1]
        return half[n-1]