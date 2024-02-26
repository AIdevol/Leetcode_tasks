class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        subarray = [nums[0]]
        min_element = nums[0]
        
        for num in nums[1:]:
            if len(subarray) == 3 or num - min_element > k:
                result.append(subarray)
                subarray = [num]
                min_element = num
            else:
                subarray.append(num)
                min_element = min(min_element, num)
        
        if subarray:
            result.append(subarray)
        
        if any(len(sub) != 3 for sub in result):
            return []
        else:
            return result



