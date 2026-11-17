class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost, max_cost = float('inf'), -float('inf')
        mprof = 0
        for i in prices:
            if i < min_cost:
                min_cost = i
                max_cost = -float('inf')
            else:
                max_cost = max(max_cost, i)
                mprof = max(mprof, max_cost - min_cost)
                

        return mprof