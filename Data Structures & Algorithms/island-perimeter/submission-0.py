class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 1

            if (i,j) in vis:
                return 0
            vis.add((i,j))
            perim = dfs(i, j+1)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            perim += dfs(i + 1, j)

            return perim
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)