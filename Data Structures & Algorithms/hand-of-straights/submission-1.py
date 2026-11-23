import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heap = []

        count_map = Counter(hand)
        heap = [k for k, v in count_map.items()]
        heapq.heapify(heap)
        cnt = 0
        while heap:
            smallest = heap[0]
            count_map[smallest] -= 1
            if count_map[smallest] == 0:
                _ = heapq.heappop(heap)
                del count_map[smallest]

            for ns in range(groupSize - 1):
                smallest += 1
                if count_map[smallest]:
                    count_map[smallest] -= 1
                    if count_map[smallest] == 0:
                        if heap[0] != smallest:
                            return False
                        _ = heapq.heappop(heap)
                        del count_map[smallest]
                else:
                    return False

        return True

                



            
        
