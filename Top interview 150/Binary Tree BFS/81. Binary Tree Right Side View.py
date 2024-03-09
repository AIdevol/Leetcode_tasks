class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if i == level_len - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result