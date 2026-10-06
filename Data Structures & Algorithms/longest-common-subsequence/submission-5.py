class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recurse(i,j):
            if i <= 0 or j <= 0:
                return 0
            if (i, j) in memo:          
                return memo[(i, j)]
            if text1[i-1] == text2[j-1]:
                memo[(i,j)] = 1 + recurse(i-1, j-1)
                return memo[(i, j)]

            memo[(i,j)] = max(recurse(i-1, j), recurse(i, j - 1))
            return memo[(i,j)]

        def bottom_up():
            dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

            for i in range(1,len(text1) + 1):
                for j in range(1, len(text2) + 1):
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[len(text1)][len(text2)]

        # _ = recurse(len(text1), len(text2))
        return bottom_up()
        