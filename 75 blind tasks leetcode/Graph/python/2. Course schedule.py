from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # Process nodes in the queue, reducing in-degrees of neighbors
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all nodes have in-degree 0 (no cycles)
        return all(in_degree[i] == 0 for i in range(numCourses))
