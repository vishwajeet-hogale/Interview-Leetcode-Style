from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad_list = defaultdict(list)
        inDegree = [0 for _ in range(numCourses)]
        for d,s in prerequisites:
            ad_list[s].append(d)
            inDegree[d] += 1

        start_nodes = [idx for idx, val in enumerate(inDegree) if val == 0]
        queue = deque(start_nodes)

        while queue:
            curr_node = queue.popleft()

            for j in ad_list[curr_node]:
                inDegree[j] -= 1

                if inDegree[j] == 0:
                    queue.append(j)

            del ad_list[curr_node]
        print(inDegree)
        for i in inDegree:
            if i:
                return False

        return True