class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def recurse(i, buy):
            if i >= n:
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            if buy:
                memo[(i, buy)] = max(-prices[i] + recurse(i+1, False), recurse(i+1, True))
            else:
                memo[(i, buy)] = max(prices[i] + recurse(i+1, True), recurse(i+1, False))

            return memo[(i, buy)]
        return recurse(0, True)