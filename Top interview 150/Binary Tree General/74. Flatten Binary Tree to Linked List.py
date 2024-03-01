# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            if prev:
                prev.left = None
                prev.right = node
            prev = node

def print_linked_list(head: TreeNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print("None")

# Test cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    
    Solution().flatten(root1)
    print_linked_list(root1)
