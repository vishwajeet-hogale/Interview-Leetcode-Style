from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        ad_list = defaultdict(list)
        for i, j in edges:
            ad_list[i].append(j)
            ad_list[j].append(i)

        queue = deque([0])
        visited = {0}

        while queue:
            curr_node = queue.popleft()
            for neigh_node in ad_list[curr_node]:
                if neigh_node not in visited:
                    visited.add(neigh_node)
                    queue.append(neigh_node)
        
        return len(visited) == n

