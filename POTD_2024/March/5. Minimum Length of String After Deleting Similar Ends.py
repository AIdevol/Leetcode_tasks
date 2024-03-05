class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        # Repeat until pointers meet or cross
        while left < right:
            # If characters at both ends are equal, find the longest prefix and suffix
            if s[left] == s[right]:
                char = s[left]

                # Move left pointer to the right until a different character is found
                while left < right and s[left] == char:
                    left += 1

                # Move right pointer to the left until a different character is found
                while left <= right and s[right] == char:
                    right -= 1
            else:
                # If characters are not equal, break the loop
                break

        # Calculate the length of the resulting string
        return max(0, right - left + 1)
