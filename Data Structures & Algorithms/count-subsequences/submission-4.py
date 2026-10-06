class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        m, n = len(s), len(t)
        def recurse(i,j):
            if j == 0:
                return 1

            if i == 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            num_ways = 0
            if s[i-1] == t[j-1]:
                num_ways = recurse(i-1, j-1) + recurse(i-1, j)
            else:
                num_ways =  recurse(i-1, j)

            memo[(i,j)] = num_ways
            return memo[(i,j)]

        def bottom_up():
            dp = [[0] * (n+1) for _ in range(m+1)]

            for i in range(m+1):
                dp[i][0] = 1

            for i in range(1, n+1):
                dp[0][i] = 0



            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

                    else:
                        dp[i][j] = dp[i-1][j]

            return dp[m][n]
        
        
        return bottom_up()