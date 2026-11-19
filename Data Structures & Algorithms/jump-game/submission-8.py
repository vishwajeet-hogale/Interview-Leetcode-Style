from collections import defaultdict
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = dict()
        def recurse(i):
            if i == n-1:
                memo[i] = True
                return memo[i]
            if i in memo:
                return memo[i]
            for jump in range(1, nums[i]+1):
                if recurse(i+jump):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]

        return recurse(0)
        

        