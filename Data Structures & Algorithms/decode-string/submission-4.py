from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        cnum = 0
        res = ""
        for c in s:
            if c.isdigit():
                cnum = cnum*10 + int(c)

            elif c == "[":
                stack.append(cnum)
                stack.append("[")
                cnum = 0

            elif c == "]":
                temp_s = ""
                while stack and stack[-1] != "[":
                    temp_s = stack.pop() + temp_s
                _ = stack.pop()
                num = stack.pop()

                stack.append(temp_s*num)

            else:
                stack.append(c)

        return "".join(stack)
                    

        