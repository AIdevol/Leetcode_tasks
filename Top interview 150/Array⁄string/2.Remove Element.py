class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] == val:
                nums[index] = nums[length - 1]
                length -= 1
            else:
                index += 1
        return length
