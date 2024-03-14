class Solution:
    def getMinimumDifference(self, root):
        min_diff = float('inf')
        stack = []
        node = root
        prev = None
        
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev:
                    min_diff = min(min_diff, node.val - prev.val)
                prev = node
                node = node.right
        
        return min_diff if min_diff != float('inf') else 0
