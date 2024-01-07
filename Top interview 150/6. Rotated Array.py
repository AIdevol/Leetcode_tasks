class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = k % len(nums)
        nums.reverse()
        nums[:a] = reversed(nums[:a])
        nums[a:] = reversed(nums[a:])
       
        