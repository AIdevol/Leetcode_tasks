# 121.best time to bye and sell book
#python

class Solution:
    def maxProfit(self, prices):
        small = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if small > price:
                small = price
            elif price - small > max_profit:
                max_profit = price - small

        return max_profit
