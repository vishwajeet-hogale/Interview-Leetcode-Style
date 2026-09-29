class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = dict()
        def recurse(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return memo[i]
        res = min(recurse(0), recurse(1))

        return res


        