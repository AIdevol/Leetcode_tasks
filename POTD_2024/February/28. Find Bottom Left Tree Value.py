# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = [root]
        leftmost_value = None
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == 0:
                    leftmost_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return leftmost_value

