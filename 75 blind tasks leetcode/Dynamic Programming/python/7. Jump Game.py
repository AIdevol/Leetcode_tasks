class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0  # maximum index we can reach so far
        
        for i in range(n):
            if i > max_index:
                # If we can't reach this position, then we can't reach the end of the array
                return False
            
            # Update the maximum index we can reach
            max_index = max(max_index, i + nums[i])
            
            if max_index >= n - 1:
                # If we can reach the last index, then we can reach the end of the array
                return True
        
        return True  # unreachable statement (just for completeness)