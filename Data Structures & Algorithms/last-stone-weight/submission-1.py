import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) >= 2:
            st1 = -heapq.heappop(stones)
            st2 = -heapq.heappop(stones)

            if st1 == st2:
                continue

            elif st2 < st1:
                heapq.heappush(stones, -1 * (st1 - st2))

        return -stones[0] if stones else 0



            



        