class Solution:
    def __init__(self):
        self.grid = None
    def dfs(self, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or self.grid[i][j] == 0:
            return 0
        
        self.grid[i][j] = 0
        directions = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]
        res = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n and self.grid[ni][nj]:
                res += self.dfs(ni, nj, m, n)

        return res

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m = len(self.grid)
        n = len(self.grid[0])
        marea = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1:
                    print(grid[i][j], i, j)
                    marea = max(marea, self.dfs(i,j, m, n))

        return marea

        