from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-count[cnt] for cnt in count]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while queue or heap:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time