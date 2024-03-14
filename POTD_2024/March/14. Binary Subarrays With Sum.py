class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # Dictionary to store the count of prefix sums
        
        for num in nums:
            prefix_sum += num
            count += sum_count.get(prefix_sum - goal, 0)
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count
