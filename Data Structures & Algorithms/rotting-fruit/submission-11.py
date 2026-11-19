from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        rotten = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh.append((i,j))

        queue = deque([(i, 0) for i in rotten])
        total_time = 0
        fresh_cnt = len(fresh)
        vis = set(rotten)

        while queue:
            (x,y), time = queue.popleft()
            total_time = max(time, total_time)
            directions = [
                (0, 1),
                (-1, 0),
                (0, -1),
                (1, 0)
            ]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append(((nx, ny), time + 1))
                    fresh.remove((nx, ny))
        
        return total_time if not fresh else -1


        