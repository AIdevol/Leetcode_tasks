# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#using the recursion 
"""class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs (node, num):
            if not node:
                return 0
            if not node.left and not node.right:
                return num*10 + node.val
            return dfs(node.left,num*10+node.val)+dfs(node.right,num*10+node.val)
        return dfs(root,0)
  
        """
#using the breadth first search 
'''class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total_sum = 0
        queue = [(root, root.val)]
        parent = {root: None}
        
        while queue:
            node, num = queue.pop(0)
            if not node.left and not node.right:
                current_node = node
                current_num = num
                while current_node:
                    current_node = parent[current_node]
                    if current_node:
                        current_num += current_node.val
                total_sum += current_num
            if node.left:
                queue.append((node.left, num*10 + node.left.val))
                parent[node.left] = node
            if node.right:
                queue.append((node.right, num*10 + node.right.val))
                parent[node.right] = node
                
        return total_sum'''
#using the iterative approaches
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

