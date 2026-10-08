from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        n = len(temperatures)
        res = [0] * n
        for i, val in enumerate(temperatures):
            if not stack:
                stack.append((val,i))
                continue

            top, idx = stack[-1]
            while val > top and stack:
                res[idx] = i - idx
                _ = stack.pop()
                if stack:
                    top, idx = stack[-1]

            stack.append((val, i))


        return res


        