class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        
        # build the graph
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        visited = set()
        def dfs(root, parent): # returns true if graph has no cycle
            visited.add(root)
            for node in graph[root]:
                if node == parent: # trivial cycle, skip
                    continue
                if node in visited:
                    return False
            
                if not dfs(node, root):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
