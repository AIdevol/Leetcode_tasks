# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total_sum = 0
        stack = [(root, root.val)]
        
        while stack:
            node, num = stack.pop()
            if not node.left and not node.right:
                total_sum += num
            if node.left:
                stack.append((node.left, num*10 + node.left.val))
            if node.right:
                stack.append((node.right, num*10 + node.right.val))
                
        return total_sum
