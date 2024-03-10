class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1=set(nums1)
        arr2=set(nums2)

        intersection_arr=arr1.intersection(arr2)

        return list(intersection_arr)