import heapq
class MedianFinder:

    def __init__(self):
        self.small_heap = [] # Max heap 
        self.big_heap = [] # Min heap
        self.counter = 0
        self.small_size = 0
        self.big_size = 0
        
    def balance(self):
        # 1. Fix ORDER: max of small must be <= min of big
        if self.small_heap and self.big_heap and -self.small_heap[0] > self.big_heap[0]:
            element = -heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, element)
            self.small_size -= 1
            self.big_size += 1

        # 2. Fix SIZES: difference can be at most 1
        while abs(self.small_size - self.big_size) > 1:
            if self.small_size > self.big_size:
                element = -heapq.heappop(self.small_heap)
                heapq.heappush(self.big_heap, element)
                self.small_size -= 1
                self.big_size += 1
            else:
                element = heapq.heappop(self.big_heap)
                heapq.heappush(self.small_heap, -element)   # negate going into max heap
                self.big_size -= 1
                self.small_size += 1






    def addNum(self, num: int) -> None:
        # Add to the small heap 
        # Balance 
            # Check the sizes -> If the Max in small > min in big you need to move the element
        # self.balance()
        heapq.heappush(self.small_heap, -num)
        self.small_size += 1
        self.counter += 1
        self.balance()

        # print(self.small_heap)
        # print(self.big_heap)
        
        
        

    def findMedian(self) -> float:
        # If the counter is odd then return min of big heap 
        # IF counter is even then return max of avg(small heap + min of big heap )
        # print(self.small_heap)
        # print(self.big_heap)
        if self.small_size > self.big_size:
            return -self.small_heap[0]
        if self.big_size > self.small_size:
            return self.big_heap[0]
        return 0.5 * (self.big_heap[0] + -self.small_heap[0])



            

            

        
        

