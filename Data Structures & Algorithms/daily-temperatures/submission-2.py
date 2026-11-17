from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = deque()
        stack.append((temperatures[0], 0))

        for i in range(1, n):
            curr_temp = temperatures[i]
            while stack and curr_temp > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                _ = stack.pop()
            
            stack.append((curr_temp, i))
        return res
        

