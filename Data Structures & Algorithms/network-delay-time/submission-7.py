from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        ad_list = defaultdict(list)
        for s,d,t in times:
            ad_list[s].append((d,t))


        dis = [float('inf') for _ in range(n+1)]
        dis[k] = 0


        queue = [(k, 0)]
        queue = deque(queue)

        while queue:
            node, total_time = queue.popleft()
            if dis[node] < total_time:
                continue

            # min_time = max(min_time, dis[node])
            for next_node, curr_time in ad_list[node]:
                if total_time + curr_time < dis[next_node]:
                    dis[next_node] = total_time + curr_time
                    
                    queue.append((next_node,total_time + curr_time ))
        # print(dis)
        min_time = max(dis[1:])
        return -1 if min_time == float('inf') else min_time

        