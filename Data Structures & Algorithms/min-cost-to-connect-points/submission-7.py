from collections import defaultdict
import heapq
class Solution:
    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # List of points, now we need a way to get a list with point and distances.
        res = []
        n = len(points)
        point_map = defaultdict(list)
        for i in range(0,n):
            for j in range(i+1, n):
                d = self.manhattan(points[i], points[j])
                point_map[tuple(points[i])].append((d, points[i], points[j]))
                point_map[tuple(points[j])].append((d, points[j], points[i]))

        vis = dict({tuple(point): 0 for point in points})
        start = tuple(points[0])
        vis[start] = 1
        queue = point_map[start]
        heapq.heapify(queue)
        cost = 0
        while queue:
            w, node, next_node = heapq.heappop(queue)
            node = tuple(node)
            next_node = tuple(next_node)
            if vis[next_node] == 0:
                vis[next_node] = 1
                cost += w

                for next_point in point_map[next_node]:
                    heapq.heappush(queue, next_point)

        return cost
