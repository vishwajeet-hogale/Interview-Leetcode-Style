import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = Counter(tasks)
        task_heap = [-count for _, count in task_map.items()]
        heapq.heapify(task_heap)
        queue = deque()
        cycle = 0
        while task_heap or queue:
            # If tasks present in the queue priritise the task 
            cycle += 1

            if queue and cycle == queue[0][0]:
                _, cnt = queue.popleft()
                heapq.heappush(task_heap, cnt)
                
            if task_heap:
                task_cnt = heapq.heappop(task_heap)
                if (task_cnt + 1) < 0:
                    queue.append((cycle + 1 + n, task_cnt + 1))


        return cycle
            
