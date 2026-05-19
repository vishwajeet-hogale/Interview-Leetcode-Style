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
        # Step 1: Build the graph and in-degree array
        # adj is a dictionary mapping a course to the list of courses that depend on it.
        # in_degree counts how many prerequisites each course has.
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for pre, course in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1

        # Step 2: Pre-compute all prerequisites for each course
        # all_prereqs will store a set of all direct and indirect prerequisites for each course.
        all_prereqs = [set() for _ in range(numCourses)]
        
        # Initialize a queue with courses that have no prerequisites (in-degree of 0).
        queue = deque([i for i, degree in enumerate(in_degree) if degree == 0])

        while queue:
            course = queue.popleft()
            
            # For each neighbor of the current course, update its prerequisites
            for neighbor in adj[course]:
                # The neighbor's prerequisites include the current course itself
                # plus all of the current course's prerequisites.
                all_prereqs[neighbor].add(course)
                all_prereqs[neighbor].update(all_prereqs[course])
                
                # Decrement the in-degree and add the neighbor to the queue if it has no more pending prerequisites
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 3: Answer the queries using the pre-computed sets
        # For each query [u, v], check if u is in the set of prerequisites for v.
        result = [u in all_prereqs[v] for u, v in queries]
        
        return result

# Example Usage:
# sol = Solution()
# numCourses = 5
# prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
# queries = [[0, 4], [4, 0], [1, 3], [3, 0]]
# print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))
# Expected output: [True, False, True, False]
