class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums, reverse=True)
        
        result = []
        for num in sorted_nums:
            added = False
            for row in result:
                if num not in row:
                    row.append(num)
                    added = True
                    break
            if not added:
                result.append([num].copy())
        
        return result
