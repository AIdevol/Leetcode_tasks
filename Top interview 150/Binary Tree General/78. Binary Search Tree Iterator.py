# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inOrderTraversal(self, root, queue):
        if (root is None):
            return
        self.inOrderTraversal(root.left, queue)
        queue.append(root.val)
        self.inOrderTraversal(root.right, queue)

    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        self.inOrderTraversal(root, self.queue)

    def next(self) -> int:
        return self.queue.pop(0)
        
    def hasNext(self) -> bool:
        return self.queue != []