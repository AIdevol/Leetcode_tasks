class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # Count incoming edges for each node
        in_degree = [0] * numCourses
        
        # Populate graph and calculate in-degrees
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1
        
        # Initialize a queue with nodes having in-degree 0
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        # Initialize a list to store the order of courses
        course_order = []
        
        # Perform topological sort
        while queue:
            course = queue.popleft()
            course_order.append(course)
            
            # Decrement in-degree of adjacent nodes
            for adjacent_course in graph[course]:
                in_degree[adjacent_course] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[adjacent_course] == 0:
                    queue.append(adjacent_course)
        
        # If all courses are included, return the course order
        if len(course_order) == numCourses:
            return course_order
        else:
            return []
