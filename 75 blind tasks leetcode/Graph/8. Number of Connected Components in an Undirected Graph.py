from collections import defaultdict

class Solution:
    def countComponents(self, n, edges):
        adj = defaultdict(list)
        self.init(adj, edges, n)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(adj, i, visited)
        return count
    
    def dfs(self, adj, index, visited):
        visited[index] = True
        for j in adj[index]:
            if not visited[j]:
                self.dfs(adj, j, visited)
    
    def init(self, adj, edges, n):
        for i in range(n):
            adj[i] = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

