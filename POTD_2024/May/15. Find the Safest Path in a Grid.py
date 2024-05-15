class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        # Initialize all thief positions
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0

        # Multi-source BFS to calculate minimum distance to any thief
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Use priority queue to find path with maximum safeness factor
        max_heap = [(-dist[0][0], 0, 0)]
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = dist[0][0]

        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            d = -d
            if r == n - 1 and c == n - 1:
                return d  # Reached bottom-right corner

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(d, dist[nr][nc])
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nr, nc))

        return -1  # In case there's no valid path