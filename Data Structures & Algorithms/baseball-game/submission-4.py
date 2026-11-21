from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = 0
        stack = deque()
        curr_num = 0
        for c in operations:
            if c in ["+", "D", "C"]:
                if stack and c == "+":
                    summed_val = int(stack[-1]) + int(stack[-2])
                    s += summed_val
                    stack.append(str(summed_val))
                elif c == "C":
                    val = stack.pop()
                    s -= int(val)
                elif stack and c == "D":
                    doubled = int(stack[-1]) * 2
                    s += doubled
                    stack.append(str(doubled))

            else:
                s += int(c)
                stack.append(c)

        return s
                


