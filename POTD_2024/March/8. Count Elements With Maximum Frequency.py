from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        max_freq = max(hashmap.values())
        total_frequency = 0
        for val in hashmap.values():
            if val == max_freq:
                total_frequency += val
        return total_frequency
