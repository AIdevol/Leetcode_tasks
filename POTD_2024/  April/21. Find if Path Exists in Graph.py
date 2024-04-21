class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS initialization
        queue = deque([source])
        visited = set([source])
        
        # Perform BFS
        while queue:
            node = queue.popleft()
            
            # Check if we reached the destination
            if node == destination:
                return True
            
            # Explore the neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # If BFS completes without finding destination
        return False
