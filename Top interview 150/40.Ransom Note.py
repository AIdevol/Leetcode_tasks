from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        char_counts = defaultdict(int)
        for char in magazine:
            char_counts[char] += 1
        
        for char in ransomNote:
            if char_counts[char] > 0:
                char_counts[char] -= 1
            else:
                return False
        
        return True
