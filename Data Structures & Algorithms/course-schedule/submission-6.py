from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for _ in range(numCourses)]
        
        ad_list = defaultdict(list)

        for dst, src in prerequisites:
            ad_list[src].append(dst)
            inDegree[dst] += 1
        queue = []
        for node, indeg_count in enumerate(inDegree):
            if indeg_count == 0:
                queue.append(node)

        queue = deque(queue)
        while queue:
            curr_node = queue.popleft()
            for adj_node in ad_list[curr_node]:
                inDegree[adj_node] -= 1
                if inDegree[adj_node] == 0:
                    queue.append(adj_node)

        return sum(inDegree) == 0



                
        