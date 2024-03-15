# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result=[1]*len(nums)
#         prefix=1
#         for i in range(len(nums)):
#             result[i]=prefix
#             prefix*=nums[i]
#         postfix=1
#         for i in range(len(nums)-1,-1,-1):
#             result[i]*=postfix
#             postfix*=nums[i]
#         return 
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
        
        # Calculate answer
        answer = [prefix_products[i] * suffix_products[i] for i in range(n)]
        
        return answer

# Example usage:
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
