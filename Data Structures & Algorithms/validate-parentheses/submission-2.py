from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_close_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in ["{", "(", "["]:
                stack.append(c)
            elif stack and stack[-1] == open_close_map[c]:
                stack.pop()

            else:
                return False

        return not stack
        



        # You have characters, it can be open or close right. Then everytime you push you start the open and then next time you pop the top should match the open barcket's closing pair. If the stack is empty and there is no open brackets left then you return False. In the end if the stack is empty then return True since you've processed all teh brackets and if it is not empty that means some bracket did not find its pair