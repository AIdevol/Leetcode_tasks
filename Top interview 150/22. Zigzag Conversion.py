class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        result = [' '] * len(s)
        total_column = len(s) // (2 * numRows - 2)
        total_rest = len(s) % (2 * numRows - 2)
        vec = [0] * numRows
        
        for i in range(1, total_rest + 1):
            if i <= numRows:
                vec[i - 1] += 1
            else:
                vec[2 * numRows - 1 - i] += 1
        
        nums = 0
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                nums += total_column + vec[i]
            else:
                nums += 2 * total_column + vec[i]
            vec[i] = nums
        
        for i in range(len(s)):
            column = (i + 1) // (2 * numRows - 2)
            rest = (i + 1) % (2 * numRows - 2)
            
            if rest == 1:
                index = column + 1
            elif rest == 0:
                index = vec[0] + (numRows > 2 and 2 or 1) * column
            elif rest == numRows:
                index = vec[numRows - 2] + column + 1
            elif 1 < rest < numRows:
                row = rest - 1
                index = vec[row - 1] + 2 * column + 1
            else:
                row = 2 * numRows - 1 - rest
                index = vec[row - 1] + 2 * column + 2
            
            result[index - 1] = s[i]
        
        return ''.join(result)

