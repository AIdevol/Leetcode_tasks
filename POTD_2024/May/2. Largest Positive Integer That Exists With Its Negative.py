class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largest_num=-1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == -nums[j] and nums[i] > 0:
                    largest_num = max(largest_num, nums[i])
        return largest_num  
