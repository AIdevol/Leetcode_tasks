class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        return max_depth