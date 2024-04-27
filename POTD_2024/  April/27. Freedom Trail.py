class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        import sys

        n = len(ring)
        m = len(key)
        char_positions = defaultdict(list)
        for index, char in enumerate(ring):
            char_positions[char].append(index)

        # DP array, initially set to a large number
        dp = [[sys.maxsize] * n for _ in range(m)]
        
        # Initialize for the first character in key
        for j in char_positions[key[0]]:
            dp[0][j] = min(j, n - j) + 1  # Clockwise and anticlockwise distances

        # Fill the dp table
        for i in range(1, m):
            for j in char_positions[key[i]]:
                for k in char_positions[key[i-1]]:
                    dist = abs(j - k)
                    step_cost = min(dist, n - dist)  # Minimum of clockwise or anticlockwise
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + step_cost + 1)
        
        # Find the minimum steps in the last row of dp
        return min(dp[m-1])