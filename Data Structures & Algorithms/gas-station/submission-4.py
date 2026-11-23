class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [g - c for g, c in zip(gas, cost)]
        n = len(diff)
        st = 0
        total = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0
                st = i + 1
            
        return -1 if st == n else st 