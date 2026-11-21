from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue

            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] += (i - stack[-1][1])
                _ = stack.pop()

            stack.append((temp, i))

        return res










        

