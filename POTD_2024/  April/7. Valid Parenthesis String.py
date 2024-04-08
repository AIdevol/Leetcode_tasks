class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0
    
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open = max(min_open - 1, 0)
                max_open -= 1
                if max_open < 0:  # More ')' than '(' or '*' seen so far
                    return False
            else:  # char == '*'
                min_open = max(min_open - 1, 0)  # Treat '*' as ')'
                max_open += 1  # Treat '*' as '('
        
        return min_open == 0