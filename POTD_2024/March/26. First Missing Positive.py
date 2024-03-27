class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Perform cyclic sort to place each number at its correct index
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        # Find the smallest positive integer that is missing
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1