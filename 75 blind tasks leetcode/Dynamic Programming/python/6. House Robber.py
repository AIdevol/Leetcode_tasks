class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

    # Initialize an array to store the maximum amount of money robbed up to each house
        dp = [0] * len(nums)

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill in the rest of the array using dynamic programming
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element of dp contains the maximum amount of money that can be robbed
        return dp[-1]
