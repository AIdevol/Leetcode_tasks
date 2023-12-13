# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

         smaller = min(p.val, q.val)
         bigger = max(p.val, q.val)

         if root:
            if root.val >= smaller and root.val <= bigger:
                return root
            elif root.val < smaller: 
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.val > bigger:
                return self.lowestCommonAncestor(root.left, p, q)