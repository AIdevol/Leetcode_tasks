class Solution:
    def containingNumber():
        if () is True:
            return True
        if {} is True:
            return True
        if [] is True:
            return True
        else:
            return False
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            elif not stack or mapping[stack.pop()] != c:
                return False
        return not stack
        