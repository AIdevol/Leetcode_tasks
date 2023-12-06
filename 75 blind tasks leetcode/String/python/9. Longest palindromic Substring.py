class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""

        start, end, length = 0, 0, 0
        for i in range(len(s)):
            len1 = self.expand_from_middle(s, i, i)
            len2 = self.expand_from_middle(s, i, i + 1)
            length = max(len1, len2)

            if end - start < length:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expand_from_middle(self, s: str, left: int, right: int) -> int:
        if not s or left > right:
            return 0

        while left >= 0 and right < len(s) and s[right] == s[left]:
            left -= 1
            right += 1

        return right - left - 1
