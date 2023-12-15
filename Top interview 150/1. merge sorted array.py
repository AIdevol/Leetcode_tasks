class Solution:
    def merge(self, nums1, m, nums2, n):
        v3 = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                v3.append(nums2[j])
                j += 1
            else:
                v3.append(nums1[i])
                i += 1

        while i < m
            v3.append(nums1[i])
            i += 1

        while j < n:
            v3.append(nums2[j])
            j += 1

        nums1[:] = v3
