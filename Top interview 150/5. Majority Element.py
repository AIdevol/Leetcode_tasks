class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=len(nums)
        n=len(nums)//2
        while x!=0:
            if(nums.count(nums[x-1])>n):
                return nums[x-1]
            else:
                x-=1