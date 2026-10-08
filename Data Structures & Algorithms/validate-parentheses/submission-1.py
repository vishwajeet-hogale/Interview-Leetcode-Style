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
        