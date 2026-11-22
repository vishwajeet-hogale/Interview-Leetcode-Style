class StockSpanner:

    def __init__(self):
        self.stack = []  

    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            _, span = self.stack.pop()
            res += span
        self.stack.append((price, res))
        return res

            