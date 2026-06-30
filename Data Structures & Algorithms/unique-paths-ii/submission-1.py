class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = dict()
        def recurse(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            directions = [
                (0,1),
                (1,0)
            ]
            num_ways = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                num_ways += recurse(ni, nj)
            
            memo[(i,j)] = num_ways
            return memo[(i,j)]

        return recurse(0,0)
        