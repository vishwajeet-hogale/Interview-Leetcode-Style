class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = dict()
        def recurse(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            directions = [
                (0,1),
                (1,0)
            ]

            num_ways = float('inf')
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    num_ways = min(grid[i][j] + recurse(ni, nj), num_ways)
                # print(num_ways)
            memo[(i,j)] = num_ways
            return memo[(i,j)]

        _ = recurse(0,0)
        return recurse(0,0)