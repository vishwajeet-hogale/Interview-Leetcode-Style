from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap = defaultdict(int)

        for i in bills:
            hmap[i] += 1
            if i == 20:
                change = 15
                if hmap[10]>0:
                    hmap[10] -= 1
                    change -= 10

                while hmap[5] > 0 and change > 0:
                    hmap[5] -= 1
                    change -= 5
                if change != 0:
                    return False

            elif i == 10:
                if hmap[5]>0:
                    hmap[5] -= 1
                    continue
                return False

            
        return True

        