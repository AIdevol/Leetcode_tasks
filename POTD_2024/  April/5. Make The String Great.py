class Solution:
    def makeGood(self, s: str) -> str:
        #our final solution, initially contains the first letter of s (because s.length >= 1)
        res = [s[0]]

        #the difference between the ASCII codes of an uppercase and lowercase letter
        letter_diff = ord("a") - ord("A")

        for i in range(1, len(s)):
            #we are iterating through each character in s, and we only add a char to the solution if:
            #   1. res is empty (so adding any character still makes the string great)
            #   2. the proposed character s[i] is not the reverse case of the last character in our solution
            if not res or abs(ord(s[i]) - ord(res[-1])) != letter_diff:
                res.append(s[i])
            #if we can't add s[i] to our solution, that means we have to delete its corresponding pair in the original string
            #this corresponds to popping the last character from our solution
            else:
                res.pop()
                
        return "".join(res)