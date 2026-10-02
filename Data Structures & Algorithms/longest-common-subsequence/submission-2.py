class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recurse(i,j):
            if i <= 0 or j <= 0:
                return 0
            if (i, j) in memo:          # the missing check
                return memo[(i, j)]
            if text1[i-1] == text2[j-1]:
                memo[(i,j)] = 1 + recurse(i-1, j-1)
                return memo[(i, j)]

            memo[(i,j)] = max(recurse(i-1, j), recurse(i, j - 1))
            return memo[(i,j)]

        _ = recurse(len(text1), len(text2))
        return memo[(len(text1), len(text2))]
        