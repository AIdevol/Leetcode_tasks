class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointer1, pointer2 = 0, 0
        min_common = float('inf')  # Initialize with positive infinity

        # Iterate until one of the arrays ends
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            # If both elements are equal, update min_common if it's smaller
            if nums1[pointer1] == nums2[pointer2]:
                min_common = min(min_common, nums1[pointer1])
                # Move both pointers to check for more common elements
                pointer1 += 1
                pointer2 += 1
            # If nums1[pointer1] is smaller, move pointer1 forward
            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            # If nums2[pointer2] is smaller, move pointer2 forward
            else:
                pointer2 += 1

        # If min_common remains infinity, there was no common element
        if min_common == float('inf'):
            return -1
        else:
            return min_common