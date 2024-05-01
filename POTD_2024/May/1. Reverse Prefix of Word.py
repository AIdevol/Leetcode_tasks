class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_occurances = word.find(ch)

        if first_occurances != -1:
            return word[:first_occurances + 1][:: -1] + word[first_occurances + 1:]

        return word