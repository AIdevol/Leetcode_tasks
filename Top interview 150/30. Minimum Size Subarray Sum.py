class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        sum = 0
        min_len = float('inf')
        
        while right < n:
            sum += nums[right]
            right += 1
            
            while sum >= target:
                min_len = min(min_len, right - left)
                sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0