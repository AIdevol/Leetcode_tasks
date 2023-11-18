class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            
            # left half of array is sorted
            if nums[mid] >= nums[left]:
                # target is in left half of array
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            # right half of array is sorted
            else:
                # target is in right half of array
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1