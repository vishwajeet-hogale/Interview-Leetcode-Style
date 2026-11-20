from collections import deque
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(e, p, i) for i, (e, p) in enumerate(tasks)], key=lambda x: x[0])
        heap = []

        time = tasks[0][0]
        res = []
        i, n = 0, len(tasks)
        while heap or i < n:
            while i < n and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not heap:
                time = tasks[i][0]
            else:
                p_t, idx = heapq.heappop(heap)
                res.append(idx)
                time += p_t

        return res



            

        