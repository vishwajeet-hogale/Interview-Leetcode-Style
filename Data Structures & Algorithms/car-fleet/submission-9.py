from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [[pi, si] for pi, si in zip(position, speed)]
        cars = sorted(cars, key = lambda x: x[0])
        time = [(target - pi) / si for pi, si in cars]

        stack = deque()
        # print(time)
        for ti in time[::-1]:

            if not stack:
                stack.append(ti)
                continue

            if stack[-1] < ti:
                stack.append(ti)
            
        return len(stack) 
        