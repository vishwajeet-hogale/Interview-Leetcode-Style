from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = deque()

        m, n = len(heights), len(heights[0])

        best = [[float('inf')] * n for _ in range(m)]
        best[0][0] = 0
        queue.append(((0,0), 0)) 
        min_answer = -float('inf')
        while queue:
            (x,y), route_diff = queue.popleft()
            
            directions = [
                (0,1),
                (0,-1),
                (1, 0),
                (-1, 0)
            ]




            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and max(route_diff, abs(heights[nx][ny] - heights[x][y])) < best[nx][ny]:
                    best[nx][ny] = max(route_diff, abs(heights[nx][ny] - heights[x][y]))
                    queue.append(((nx, ny), best[nx][ny]))

         

        return best[m-1][n-1]

        