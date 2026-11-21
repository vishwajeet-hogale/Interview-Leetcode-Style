from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque([asteroids[0]])

        for i, stone in enumerate(asteroids):
            if i < 1:
                continue
            
            while stack and stack[-1] > 0 and stone < 0:

                if abs(stone) > stack[-1]:
                    _ = stack.pop()
                    continue

                if abs(stone) == abs(stack[-1]):
                    _ = stack.pop()

                break
            else:
                stack.append(stone)

        return list(stack)

        


        