class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        length = len(nums)
        frequency_map = {}  # Dictionary to store the frequency of elements
        
        max_length = 0  # Variable to store the maximum length of the subarray with frequency <= k
        
        # Loop through the array using two pointers: start and end
        while end < length:
            frequency_map[nums[end]] = frequency_map.get(nums[end], 0) + 1  # Update frequency
            
            # If the frequency of the element exceeds 'k', adjust the window by moving 'start' pointer
            if frequency_map[nums[end]] > k:
                while start < end and frequency_map[nums[end]] > k:
                    # Shrink the window by moving 'start' pointer and updating frequency_map
                    if frequency_map[nums[start]] == 1:
                        del frequency_map[nums[start]]  # Remove element if its count is 1
                    else:
                        frequency_map[nums[start]] -= 1  # Decrement frequency
                    start += 1
                
            max_length = max(max_length, end - start + 1)  # Update max_length for each iteration
            end += 1
        
        return max_length  # Return the maximum length of the subarray with frequency <= k

