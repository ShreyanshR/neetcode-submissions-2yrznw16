class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = 0

        
        for s in range(1, len(prices)):
            if prices[b] <= prices[s]:
                profit = max(profit, prices[s] - prices[b])
                s += 1
            else:
                b = s
            

        return profit

        