# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # dfs
#         if not edges:
#             return [0]

#         graph = collections.defaultdict(list)
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)

#         leaves = []
#         for node in graph:
#             if len(graph[node]) == 1:
#                 leaves.append(node)

#         while n > 2:
#             n -= len(leaves)
#             new_leaves = []
#             for leaf in leaves:
#                 neighbor = graph[leaf].pop()
#                 graph[neighbor].remove(leaf)
#                 if len(graph[neighbor]) == 1:
#                     new_leaves.append(neighbor)
#             leaves = new_leaves

#         return leaves
# ___________________________________________________________________________________________________
#toplogical method
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n == 1:
#             return [0]
        
#         # Step 1: Build the graph
#         from collections import defaultdict, deque
#         graph = defaultdict(list)
#         degree = [0] * n
        
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
#             degree[u] += 1
#             degree[v] += 1
        
#         # Step 2: Initialize leaves
#         leaves = deque()
#         for i in range(n):
#             if degree[i] == 1:
#                 leaves.append(i)
        
#         # Step 3: Remove leaves layer by layer
#         remaining_nodes = n
#         while remaining_nodes > 2:
#             leaves_count = len(leaves)
#             remaining_nodes -= leaves_count
#             for _ in range(leaves_count):
#                 leaf = leaves.popleft()
#                 for neighbor in graph[leaf]:
#                     degree[neighbor] -= 1
#                     if degree[neighbor] == 1:
#                         leaves.append(neighbor)
        
#         # Step 4: Return the last set of leaves
#         return list(leaves)
# ------------------------------------------------------------------------------------
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = [node for node in graph if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves