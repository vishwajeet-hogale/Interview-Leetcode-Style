from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        s = 0
        for op in operations:
            if op not in ["+", "C", "D"]:
                stack.append(int(op))
                s += int(op)

            elif op == "D" and stack:
                num1 = int(stack[-1])
                stack.append(num1*2)
                s += num1*2
            elif op == "+" and len(stack) >= 2:
                num1 = int(stack[-1])
                num2 = int(stack[-2])
                s += num1 + num2
                stack.append(num1 + num2)

            else:
                if stack:
                    num1 = int(stack.pop())
                    s -= num1
        return s
                

