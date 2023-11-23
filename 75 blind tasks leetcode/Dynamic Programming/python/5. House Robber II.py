from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1] if n > 1 else 0)

        for i in range(2, n):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr

        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        v1 = nums[1:]
        v2 = nums[:-1]

        ans = max(self.solve(v1), self.solve(v2))
        return ans
