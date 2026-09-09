from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        rotten = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                if grid[i][j] == 2:
                    rotten.append((i,j))

        queue = [[point, 0] for point in rotten]
        time = 0                                    # was float('inf')
        queue = deque(queue)

        while queue:
            curr_fruit, t = queue.popleft()
            i,j = curr_fruit
            time = max(t, time)                     # was min

            directions = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            ]

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) in fresh:
                    grid[ni][nj] = 2
                    fresh.remove((ni,nj))
                    queue.append([[ni, nj], t + 1])

        if fresh:                                   # the -1 case
            return -1

        return time