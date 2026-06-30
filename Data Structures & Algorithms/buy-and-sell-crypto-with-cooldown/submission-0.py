class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recurse(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]

            profit = 0
            # Case 1 : Buy 
            if buy:
                profit = max(-prices[i] + recurse(i+1, False), recurse(i+1, True))
            else:
                # Sell case: increment index by 2 due to 1-day cooldown
                profit = max(prices[i] + recurse(i+2, True), recurse(i+1, False))
            
            memo[(i, buy)] = profit
            return profit

        return recurse(0, True)