class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            current = n
            sum_of_digits = 0
            while current:
                digit = current % 10
                sum_of_digits += digit * digit
                current //= 10
            if sum_of_digits in seen:
                return False
            seen.add(sum_of_digits)
            n = sum_of_digits
        return True
