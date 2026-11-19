from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append(((i,j), 0))
        
        while queue:
            (x,y), cdis = queue.popleft()

            directions = [
                (0,1),
                (-1, 0),
                (1, 0),
                (0, -1)
            ]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and cdis + 1 < grid[nx][ny]:
                    grid[nx][ny] = 1 + cdis
                    queue.append(((nx, ny), cdis + 1))
        

