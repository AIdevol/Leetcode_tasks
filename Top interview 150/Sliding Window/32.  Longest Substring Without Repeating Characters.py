class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        summ = 0
        l = 0 
        for r in range(len(s)):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                summ = max(summ,r-l+1)
            else:
                l = l + 1
        return summ