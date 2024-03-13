from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])
        i = 0
        
        while queue:
            sz = len(queue)
            v = []
            
            for _ in range(sz):
                f = queue.popleft()
                v.append(f.val)
                
                if f.left:
                    queue.append(f.left)
                if f.right:
                    queue.append(f.right)
            
            if i % 2:
                v.reverse()
            ans.append(v)
            i += 1
        
        return ans

# Test case
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]
