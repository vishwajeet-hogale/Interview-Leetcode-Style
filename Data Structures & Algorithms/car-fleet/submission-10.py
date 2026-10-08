from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [[pi, si] for pi, si in zip(position, speed)]
        cars = sorted(cars, key = lambda x: x[0])
        time = [(target - pi) / si for pi, si in cars]

        stack = deque()

        for ti in time[::-1]:

            if not stack:
                stack.append(ti)
                continue

            if stack[-1] < ti:
                stack.append(ti)
            
        return len(stack) 
        

        # The idea is that you start from the last position if any prev cars arrive at the destination faster than the cars ahead, they merge with cars ahead. so the condition is cars that reach first and then you compare their time if them come after the stack's most recent time (top essentially) then you push it to teh stack. If they come earlier, we don't push to stack that means they merged with the cars ahead