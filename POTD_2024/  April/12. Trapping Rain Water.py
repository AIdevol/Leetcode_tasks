class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n
        volume = 0

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, n - 1):
            trapped_water = max(0, min(left_max[i - 1], right_max[i + 1]) - height[i])
            volume += trapped_water

        return volume