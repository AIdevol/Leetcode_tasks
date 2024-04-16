# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val (d-1)
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #  (depth-1) depth==1 ,val
        
        if depth == 1: return TreeNode(val,root,None )
        elif depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)

        else:
            if root.left: self.addOneRow(root.left, val, depth-1)
            if root.right: self.addOneRow(root.right,val,depth-1)

        return root