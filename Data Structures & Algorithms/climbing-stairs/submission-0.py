class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(n):
            if  n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = recurse(n-1) + recurse(n-2)
            return memo[n]

        return recurse(n)
        