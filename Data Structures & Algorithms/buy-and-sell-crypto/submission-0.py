class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = float('inf')
        profit = 0
        for price in prices:
            if price < min1:
                min1 = price
            else:
                profit = max(profit, price-min1)
        
        return profit