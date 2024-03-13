class Solution:
    def pivotInteger(self, n: int) -> int:
        return int(i) if (i:=sqrt(n*(n+1)/2)).is_integer() else -1