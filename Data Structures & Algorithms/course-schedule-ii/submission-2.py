from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ad_list = defaultdict(list)
        queue = []
        inDegree = [0 for _ in range(numCourses)]

        for dst, src in prerequisites:
            ad_list[src].append(dst)
            inDegree[dst] += 1
        for node in range(numCourses):
            if inDegree[node] == 0:
                queue.append(node)

        queue = deque(queue)
        res = []
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)
            for adj_node in ad_list[curr_node]:
                inDegree[adj_node] -= 1
                if inDegree[adj_node] == 0:
                    queue.append(adj_node)


        return res if sum(inDegree) == 0 else []

        