class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def recurse(i,j):
            if i < 0 or i >= m or j < 0 or j >=n:
                return 0
            if (i,j) in memo:
                return memo[(i, j)]
            if i == m - 1 and j == n - 1:
                return 1

            directions = [
                (1,0),
                (0,1)
            ]
            res = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    res += recurse(ni, nj)

            memo[(i, j)] = res
            return memo[(i, j)]

        def bottom_up():
            dp = [[1 for _ in range(n)] for _ in range(m)]
            # for i in range(1, n):
            #     dp[0][i] = dp[0][i-1] + 1
            # for i in range(1, m):
            #     dp[i][0] = dp[i-1][0] + 1

            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

            return dp[m-1][n-1]
            
            

        return bottom_up()
            
        