class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_price, max_price = float('inf'), -float('inf')
        for price in prices:
            if min_price > price:
                min_price = price
                continue

            profit = max(profit, price - min_price)

        return profit

        