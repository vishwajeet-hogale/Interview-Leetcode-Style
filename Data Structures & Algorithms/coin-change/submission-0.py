class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        def recurse(i, amount):
            if amount == 0:
                return 0
            if i == 0:
                return float('inf')

            if coins[i-1] <= amount:
                return min(1 + recurse(i, amount - coins[i-1]), recurse(i-1, amount))

            return recurse(i-1, amount)

        def dp():
            n = len(coins)
            dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
            # When you have no coins -> you can make infinity sum
            for i in range(amount + 1):
                dp[0][i] = float('inf')

            # When you have many coins but amount is 0 then you need zero coins
            for i in range(n+1):
                dp[i][0] = 0

            for i in range(1,n+1):
                for j in range(1, amount+1):
                    if j >= coins[i-1]:
                        dp[i][j] = min(1 + dp[i][j - coins[i-1]], dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]

            return dp[n][amount]
            




        res = dp()
        return  -1 if res == float('inf') else res
        