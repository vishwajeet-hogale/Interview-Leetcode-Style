class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def recurse(i, buy=True):
            if i >= n:
                return 0
                
            if (i,buy) in memo:
                return memo[(i,buy)]

            profit = 0
            if buy:
                profit = max(-prices[i] + recurse(i+1, not buy), recurse(i+1, buy))

            else:
                profit = max(prices[i] + recurse(i+2, not buy), recurse(i+1, buy))

            memo[(i,buy)] = profit
            return memo[(i,buy)]

        return recurse(0)


