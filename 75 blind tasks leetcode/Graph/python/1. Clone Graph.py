from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        
        visited = {}
        return self.cloneGraphHelper(node, visited)
    
    def cloneGraphHelper(self, node: Node, visited: dict) -> Node:
        if node in visited:
            return visited[node]
        
        copy = Node(node.val)
        visited[node] = copy
        
        for neighbor in node.neighbors:
            neighborCopy = self.cloneGraphHelper(neighbor, visited)
            copy.neighbors.append(neighborCopy)
        
        return copy

