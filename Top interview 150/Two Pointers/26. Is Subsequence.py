class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1,t1 = 0 ,0

        while s1< len(s) and t1<len(t):
            if s[s1] == t[t1]:
                s1 += 1
            t1 += 1
        
        return s1 ==len(s)