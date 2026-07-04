class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = right = 0
        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
            elif prices[i] > prices[left]:
                curr = prices[i] - prices[left]
                if curr > profit:
                    profit = curr
                right = i


            
        return profit