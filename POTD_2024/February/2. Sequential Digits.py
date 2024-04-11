class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_digits = "123456789"
        result = []

        str_low= str(low)
        str_high = str(high)

        str_low, str_high = len(str_low), len(str_high)

        # i = length
        for length in range(str_low, str_high + 1):
            for start_index in range(0, 10 - length):

                substr=seq_digits[start_index:start_index + length]
                num = int(substr)

                if low <= num <= high:
                    result.append(num)

        return result
