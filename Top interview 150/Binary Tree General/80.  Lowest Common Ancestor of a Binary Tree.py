class Solution:
    def lowestCommonAncestor(self, root, n1, n2):
        if root is None:
            return None

        if root.val == n1.val or root.val == n2.val:
            return root

        leftans = self.lowestCommonAncestor(root.left, n1, n2)
        rightans = self.lowestCommonAncestor(root.right, n1, n2)

        if leftans is not None and rightans is not None:
            return root
        elif leftans is not None:
            return leftans
        elif rightans is not None:
            return rightans
        else:
            return None