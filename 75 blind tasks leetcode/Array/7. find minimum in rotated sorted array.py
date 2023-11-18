class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # right half is sorted, search left half
                right = mid
            else:
                # left half is sorted or both halves are sorted
                left = mid + 1
        # left == right, which is the index of the minimum element
        return nums[left]