class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyprice = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buyprice:
                buyprice = price
            profit = max(profit, price - buyprice)
        return profit
        