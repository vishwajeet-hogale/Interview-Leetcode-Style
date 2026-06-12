from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        dist = [[float('inf')] * c for _ in range(r)]
        dist[0][0] = 0
        queue = deque([(0, 0)])
        dirs = [(0,1), (-1,0), (0,-1), (1,0)]
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < r and 0 <= ny < c:
                    ne = max(dist[cx][cy], abs(heights[cx][cy] - heights[nx][ny]))
                    if ne < dist[nx][ny]:
                        dist[nx][ny] = ne
                        queue.append((nx, ny))
        return dist[r-1][c-1]