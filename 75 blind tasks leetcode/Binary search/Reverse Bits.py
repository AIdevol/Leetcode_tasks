class Solution:
    def reverseBits(self, n: int) -> int:
        bitstr = bin(n)[2:]
        b = len(bitstr)
        bitstr = '0' * (32 - b) + bitstr
        return int(bitstr[::-1], 2)