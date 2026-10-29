from collections import deque
class Solution:
    

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        def djkstra(i,j):
            nonlocal directions, grid
            queue = deque()
            queue.append([(i,j), 0])
            while queue:
                (i,j), cost = queue.popleft()

                if cost > grid[i][j]:
                    continue

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and cost + 1 < grid[ni][nj] and not grid[ni][nj] < 0:
                        queue.append([(ni, nj), cost + 1])
                        grid[ni][nj] = cost + 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    djkstra(i,j)
        
                    
                    
        