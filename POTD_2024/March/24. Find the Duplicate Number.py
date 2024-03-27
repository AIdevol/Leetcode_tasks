class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s_len=nums[0]
        f_len=nums[0]
        
        while True:
            s_len=nums[s_len]
            f_len=nums[nums[f_len]]
            if s_len==f_len:
                break

        s_len=nums[0]
        while s_len != f_len:
            s_len=nums[s_len]
            f_len=nums[f_len]

        return s_len

         