class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        prevPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if price > prevPrice:
                maxProfit += price - prevPrice
            prevPrice = price
        
        return maxProfit