class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        
        while True:

            while current is not None:
                stack.append(current)
                current = current.left
            
            if not stack:
                break
                
            node = stack.pop()
            k -= 1
            
            if k == 0:
                return node.val
            
            current = node.right