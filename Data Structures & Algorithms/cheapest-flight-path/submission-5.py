from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ad_list = defaultdict(list)
        for s, d, cost in flights:
            ad_list[s].append((d, cost))

        queue = deque([(src, 0, 0)])
        dis = [float('inf') for _ in range(n)]
        dis[src] = 0

        while queue:
            curr_node, cost, jumps = queue.popleft()
            if jumps - 1 >= k:
                continue
            for neigh_node, travel in ad_list[curr_node]:
                
                if (cost + travel) < dis[neigh_node] :
                    dis[neigh_node] = cost + travel
                    queue.append((neigh_node, cost + travel, jumps + 1)) 

        return -1 if dis[dst] == float('inf') else dis[dst]
