class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26  
            for char in word:
                count[ord(char) - ord('a')] += 1  # Count the occurrence of each character
            
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        
        return list(anagrams.values())
