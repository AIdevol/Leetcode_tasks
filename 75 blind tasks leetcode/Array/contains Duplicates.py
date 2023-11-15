#217. contains duplicates

#python

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table={}
        for p in range(len(nums)):
            if hash_table.get(nums[p]):
                return True
            else:
                hash_table[nums[p]]=True
        return False