class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
    
        for char in s:
            idx = ord(char) - ord('a')
          
            max_len = 0
           
            for j in range(max(0, idx - k), min(25, idx + k) + 1):
                max_len = max(max_len, dp[j])
            
            dp[idx] = max_len + 1
        
      
        return max(dp)