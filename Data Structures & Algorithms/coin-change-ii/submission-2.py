class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def recurse(i, amount):
            if i == 0:
                if amount == 0:
                    return 1
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)]
            num_ways = 0
            if coins[i-1] <= amount:
                num_ways += recurse(i, amount - coins[i-1]) + recurse(i-1, amount)

            else:
                num_ways += recurse(i-1, amount)

            memo[(i, amount)] = num_ways
            return num_ways

        n = len(coins)
        return recurse(n, amount)

            
        
        
        