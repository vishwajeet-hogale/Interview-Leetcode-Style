import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.min_heap, n)
            if len(self.min_heap) > k:
                _ = heapq.heappop(self.min_heap)

            

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            _ = heapq.heappop(self.min_heap)

        return self.min_heap[0]
        
