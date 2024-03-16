class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        # A dictionary to store the running sum and its first occurrence index
        sum_index_map = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            # If the current running sum is seen before, update max_length
            if count in sum_index_map:
                max_length = max(max_length, i - sum_index_map[count])
            else:
                sum_index_map[count] = i

        return max_length