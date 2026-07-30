class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window (Redo)

        highestProfit = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[L] < prices[R]:
                currentProfit = prices[R] - prices[L]
                highestProfit = max(highestProfit, currentProfit)
            else:
                L = R
            R += 1
        return highestProfit