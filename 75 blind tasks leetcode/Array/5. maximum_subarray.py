class Solution:
    def maxSubArray(self, nums):
        largest_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum = current_sum + nums[i]
            else:
                current_sum = nums[i]

            if current_sum > largest_sum:
                largest_sum = current_sum

        return largest_sum
