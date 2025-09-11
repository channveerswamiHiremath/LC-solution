class Solution(object):
    def maxProfit(self, prices):
        minso = prices[0]
        res = 0
        for i in range(1, len(prices)):
            minso = min(prices[i], minso)
            res = max(res, prices[i] - minso)
        return res
        