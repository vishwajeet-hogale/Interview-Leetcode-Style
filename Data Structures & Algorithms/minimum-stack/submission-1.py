from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
            return

        if self.min_stack[-1] >= val:
            # _ = self.min_stack.pop()
            self.min_stack.append(val)
        return

        

    def pop(self) -> None:
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            _ = self.min_stack.pop()

        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]





# [-2, -2, -3, -3] 

# stack -2, 

        
