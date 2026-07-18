from collections import deque
class Solution:
    def __init__(self):
        self.queue = deque()
        self.grid = None
        self.directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        self.m = -1
        self.n = -1
    def dfs(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.grid[i][j] in [0, 2]:
            return
        self.queue.append(((i,j), 0))
        self.grid[i][j] = 2

        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.m and 0 <= nj < self.n and self.grid[ni][nj] == 1:
                self.dfs(ni, nj)

        return

    def bfs(self):
        while self.queue:
            (x, y), curr_dis = self.queue.popleft()
            
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n:
                    if self.grid[nx][ny] == 0:
                        self.queue.append(((nx, ny), curr_dis + 1))
                        self.grid[nx][ny] = -1

                    elif self.grid[nx][ny] == 1:
                        return curr_dis 

        return -1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        # First do a dfs to convert land == 1 to 2 and populate the queue
        # queue = deque()
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        island_a = False
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j]:
                    self.dfs(i, j)
                    island_a = True
                    break

            if island_a:
                break

        # Second we will find the closest island 
        return self.bfs()


        