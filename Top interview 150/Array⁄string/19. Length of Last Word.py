class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        length=0
        i=len(s)-1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
