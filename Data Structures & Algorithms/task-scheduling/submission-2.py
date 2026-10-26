import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)

        queue = deque()  # (remaining_count, ready_time)
        cycle = 0
        while heap or queue:
            # 1. Release: move a cooled-down task back into the heap
            if queue and queue[0][1] == cycle:
                heapq.heappush(heap, queue.popleft()[0])

            # 2. Run: use one unit of the most frequent task, if any
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    queue.append((cnt, cycle + 1 + n))

            # 3. Tick: one slot passes, whether we ran a task or idled
            cycle += 1

        return cycle