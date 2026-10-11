import math
class Solution:
    def can_eat(self, piles, k, h):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / k)
        return hrs <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:

            k = l + (r - l) // 2
            if self.can_eat(piles, k, h):
                r = k
            else:
                l = k + 1

        return l
        