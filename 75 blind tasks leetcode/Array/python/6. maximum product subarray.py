import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod, min_prod = nums[0], nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num >= 0:
                max_prod = max(num, max_prod * num)
                min_prod = min(num, min_prod * num)
            else:
                temp = max_prod
                max_prod = max(num, min_prod * num)
                min_prod = min(num, temp * num)
            result = max(result, max_prod)
        return result
