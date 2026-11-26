from collections import Counter, deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = deque()
        star_stack = deque()

        for i, c in enumerate(s):
            if c == "(":
                open_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            else:
                if open_stack and open_stack[-1] < i:
                    _ = open_stack.pop()
                    print(open_stack)
                    print(star_stack)
                    print()
                    continue
                elif star_stack and star_stack[-1] < i:
                    _ = star_stack.pop()
                else:
                    return False


        while open_stack and star_stack:
            if star_stack[-1] < open_stack[-1]:
                return False
            _ = open_stack.pop()
            _ = star_stack.pop()
        return not open_stack


        