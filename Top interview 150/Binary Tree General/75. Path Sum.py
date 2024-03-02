# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Terminating condition
        if not root:
            return False
        
        # Subtract the current node's value from the sum
        sum -= root.val
        
        # If it's a leaf node and sum becomes zero, return True
        if sum == 0 and not root.left and not root.right:
            return True
        
        # Propagate the check to the left and right subtrees
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
