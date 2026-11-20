from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.front_stack = deque()
        self.rear_stack = deque()
        self.capacity = k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear_stack.append(value)
        self.capacity -= 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if not self.front_stack:
            while self.rear_stack:
                self.front_stack.append(self.rear_stack.popleft())
        self.front_stack.popleft()      # moved out of the if
        self.capacity += 1
        return True


    def Front(self) -> int:
        
        if not self.front_stack:
            while self.rear_stack:
                self.front_stack.append(self.rear_stack.popleft())
        return self.front_stack[0] if self.front_stack else -1
    
    def Rear(self) -> int:
        if not self.rear_stack:
            if not self.front_stack:
                return -1
            elif self.front_stack:
                return self.front_stack[-1]

        return self.rear_stack[-1]

        

    def isEmpty(self) -> bool:
        return self.capacity == self.k
        

    def isFull(self) -> bool:
        return self.capacity == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

[]