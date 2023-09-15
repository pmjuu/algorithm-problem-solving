class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min = float('inf')
        
        for price in prices:
            if (price < min):
                min = price
            else:
                max_profit = max(price - min, max_profit)
        
        return max_profit