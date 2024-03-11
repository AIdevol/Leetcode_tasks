class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_index = {char: i for i, char in enumerate(order)}

        # Sort the characters in the string 's' based on the custom order defined by the 'order' string
        sorted_s = sorted(s, key=lambda x: char_index.get(x, float('inf')))

        # Join the sorted characters to form the permuted string
        return ''.join(sorted_s)