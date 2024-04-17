# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path, smallest):
            if not node:
                return ''
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                current_string = ''.join(reversed(path))
                if not smallest[0] or current_string < smallest[0]:
                    smallest[0] = current_string
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            path.pop()
        
        smallest = [""]
        dfs(root, [], smallest)
        return smallest[0]
