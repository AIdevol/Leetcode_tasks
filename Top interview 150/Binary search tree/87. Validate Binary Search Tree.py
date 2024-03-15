class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder_traversal(node, prev):
            if not node:
                return True
            
            # Traverse left subtree
            if not inorder_traversal(node.left, prev):
                return False
            
            # Check current node's value
            if prev[0] is not None and node.val <= prev[0]:
                return False
            
            prev[0] = node.val  # Update previous node's value
            
            # Traverse right subtree
            return inorder_traversal(node.right, prev)
        
        # Start inorder traversal
        prev = [None]  # Using list to store previous node's value
        return inorder_traversal(root, prev)

# Example usage:
# Constructing example trees
tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)

tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)

# Checking validity of BSTs
solution = Solution()
print(solution.isValidBST(tree1))  # Output: True
print(solution.isValidBST(tree2))  # Output: False
