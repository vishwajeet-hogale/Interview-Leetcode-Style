from collections import deque, defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [float("inf")] * (n+1)

        adj_list = defaultdict(list)
        for s,d,t in times:
            adj_list[s].append((d, t))
        dis[0] = 0
        dis[k] = 0
        queue = deque([(k, 0, 0)])
        time = 0
        while queue:
            node, curr_dis, time = queue.popleft()
            
            for neigh_node, nex_dis in adj_list[node]:
                if curr_dis + nex_dis < dis[neigh_node]:
                    queue.append((neigh_node, curr_dis + nex_dis, time+1))
                    dis[neigh_node] = curr_dis + nex_dis


        time = max(dis[1:])
        return -1 if float("inf") in dis[1:] else time
                
        