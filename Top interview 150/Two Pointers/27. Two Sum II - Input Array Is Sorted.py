class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l < r:
            suma = numbers[l] + numbers[r]            
            if suma == target:
                return [l+1, r+1]
            elif suma > target:
                r -= 1
            else:
                l += 1
                
        return [-1, -1]
    """def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def twoSum(numbers, target):
            left, right = 0, len(numbers) - 1
            while left < right:
                sum = numbers[left] + numbers[right]

                if sum == target:
                    return [left + 1, right + 1]
                    elif sum < target:
                        left += 1

                    else:

                        right -= 1
                            return []"""
     