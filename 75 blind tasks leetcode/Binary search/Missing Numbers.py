class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)

        expected_sum = n * (n + 1) // 2  # Sum of numbers in the range [0, n]

        actual_sum = sum(nums)

        return expected_sum - actual_sum
