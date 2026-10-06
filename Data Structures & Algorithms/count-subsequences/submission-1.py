class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
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
        
        m, n = len(s), len(t)
        return recurse(m, n)