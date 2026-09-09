from collections import deque
class Solution:
    def __init__(self):
        self.grid = None
    def dfs(self, i, j, m, n):
        # Exit condition
        if  i < 0 or i >= m or j < 0 or j >= n or self.grid[i][j] == "0":
            return 
        # Goal condition
        # Visit the state
        self.grid[i][j] = "0"
        # recursive step
        directions = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and self.grid[ni][nj] == "1":
                self.dfs(ni, nj, m, n)

    def dfs_runner(self):
        m = len(self.grid)
        n = len(self.grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i, j, m, n)
        return cnt

    def bfs(self, i, j, m, n):
        q = deque([(i, j)])
        self.grid[i][j] = "0"
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            ci, cj = q.popleft()
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and self.grid[ni][nj] == "1":
                    self.grid[ni][nj] = "0"
                    q.append((ni, nj))
    def bfs_runner(self):
        m, n = len(self.grid), len(self.grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == "1":
                    cnt += 1
                    self.bfs(i, j, m, n)
        return cnt
    def numIslands(self, grid: List[List[str]]) -> int:
        if self.grid is None:
            self.grid = grid

        # Option 1 : DFS approach

        # return self.dfs_runner()

        # Option 2 : BFS
        return self.bfs_runner()


        
        