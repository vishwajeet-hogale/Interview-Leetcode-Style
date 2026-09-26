from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = deque()
        m, n = len(heights), len(heights[0])

        best = [[float('inf') for _ in range(n)] for _ in range(m)]
        best[0][0] = 0

        queue.append(((0,0), 0))

        while queue:
            (x, y), max_diff = queue.popleft()
            if best[x][y] < max_diff:
                continue
            directions = [
                (0,1),
                (1, 0),
                (-1,0),
                (0, -1)
            ]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n :
                    e = max(max_diff, abs(heights[nx][ny] - heights[x][y]))
                    if e < best[nx][ny]:
                        best[nx][ny] = e
                        queue.append(((nx,ny), e))

        return best[m-1][n-1] if best[m-1][n-1] != float('inf') else 0

