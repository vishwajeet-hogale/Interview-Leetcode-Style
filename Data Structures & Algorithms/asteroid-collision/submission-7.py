class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for stone in asteroids:

            while stack and stack[-1] > 0 and stone < 0:
                if stack[-1] < abs(stone):
                    stack.pop()
                    continue
                
                # If they are the same size, BOTH explode.
                elif stack[-1] == abs(stone):
                    stack.pop()
                
                break
            else:
                stack.append(stone)

        return stack