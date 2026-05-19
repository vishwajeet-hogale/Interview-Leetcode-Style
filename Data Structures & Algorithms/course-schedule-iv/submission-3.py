from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Determines if a course is a prerequisite for another using graph traversal.

        Args:
            numCourses: The total number of courses.
            prerequisites: A list of prerequisite pairs [pre, course].
            queries: A list of query pairs [u, v] to check.

        Returns:
            A list of booleans indicating if u is a prerequisite for v for each query.
        """
        ad_list = defaultdict(list)
        reachable = [set() for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for s,d in prerequisites:
            ad_list[s].append(d)
            indegree[d] += 1

        queue = deque([idx for idx, val in enumerate(indegree) if val == 0])

        while queue:
            curr_node = queue.popleft()
            for neigh_node in ad_list[curr_node]:
                indegree[neigh_node] -= 1
                reachable[neigh_node].add(curr_node)
                reachable[neigh_node].update(reachable[curr_node])

                if indegree[neigh_node] == 0:
                    queue.append(neigh_node)

            del ad_list[curr_node]

        res = []
        for ui, vi in queries:
            val = bool(ui in reachable[vi])
            res.append(val)

        return res