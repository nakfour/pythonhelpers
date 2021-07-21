class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<=0:
            return 0
        i = 0
        maxProfit = 0
        valley = prices[0]
        peak = prices [0]
        while i < len(prices) - 1:
            # Find the valleys
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit
