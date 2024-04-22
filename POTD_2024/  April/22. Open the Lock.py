class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d)%10
                    yield node[:i] + str(y) + node[i+1:]
        dead = set(deadends)
        if '0000' in dead:
            return -1
        queue = deque([('0000', 0)])
        visited = set(['0000'])
        
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            for neighbor in neighbors(node):
                if neighbor not in visited and neighbor not in dead:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        return -1  

        # bfs method
        # if '0000' in deadends:
        #     return -1

        # def children(lock):
        #     res = []
        #     for i in range(4):
        #         digit =str((int(lock[i])+1)% 10)
        #         res.append(lock[:i] + digit + lock[i + 1:])
        #         digit =str((int(lock[i])-1 +10)% 10 )
        #         res.append(lock[:i] + digit + lock[i + 1:])
        #     return res


        # q = deque()
        # q.append(['0000',0])
        # visit = set(deadends)
        # # deadends =set(deadends)

        # while q:
        #     lock, turns =q.popleft()
        #     if lock == target:
        #         return turns
        #     for child in children(lock):
        #         if child not in visit:
        #             visit.add(child)
        #             q.append([child, turns + 1])
        # return -1
