from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j, 0))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
        

        queue = deque(rotten)
        time = 0
        while queue:
            curr_infected_cell = queue.popleft()
            curr_x, curr_y, curr_time = curr_infected_cell
            time = curr_time
            directions = [
                (0,1),
                (-1,0),
                (1,0),
                (0, -1)
            ]

            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y, time + 1))
                    if (new_x, new_y) in fresh:
                        fresh.remove((new_x, new_y))
            

        return time if not fresh else -1
            

            