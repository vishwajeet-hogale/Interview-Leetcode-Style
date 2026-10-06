class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        memo = {}
        def recurse(i, j):
            if j >= n:
                return i>=m
            
            if (i,j) in memo:
                return memo[(i,j)]

            if j + 1 < n and p[j + 1] == "*" and recurse(i, j + 2):
                return True
            
            res = False
            # Case 1 : When there is a dot 
            if i < m and j < n and p[j] == '.':
                res = recurse(i+1, j+1)
            # Case 2 : WHen there is a * 
            elif j < n and p[j] == "*":
                match = i < m and (p[j - 1] == '.' or s[i] == p[j - 1])
                res = recurse(i, j + 1) or (match and recurse(i + 1, j))
            # Case 3: When there is a charcater and you match 
            elif i<m and j<n and s[i] == p[j]:
                res = recurse(i+1,j+1)
            else:
                res = False

            memo[(i,j)] = res
            return memo[(i,j)]

        return recurse(0,0)
            

        