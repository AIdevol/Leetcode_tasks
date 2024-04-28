class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        # Graph adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Size of each subtree
        sz = [0] * n
        # Sum of distances from node to all nodes in its subtree
        dp = [0] * n
        # Final answer: sum of distances to all other nodes
        answer = [0] * n
        
        # First DFS to calculate sz and dp arrays
        def dfs(u, parent):
            sz[u] = 1  # count itself
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
                sz[u] += sz[v]
                dp[u] += dp[v] + sz[v]

        # Second DFS to calculate the result using dp values
        def dfs2(u, parent):
            # Set the answer for the root node
            if parent == -1:
                answer[u] = dp[u]
            else:
                # Formula derived from dp[parent] and dp[child] relationships
                answer[u] = answer[parent] + (n - sz[u]) - sz[u]
            
            for v in graph[u]:
                if v == parent:
                    continue
                dfs2(v, u)
        
        # Start DFS from node 0 (assuming 0 is a node in the graph)
        dfs(0, -1)
        dfs2(0, -1)
        
        return answer