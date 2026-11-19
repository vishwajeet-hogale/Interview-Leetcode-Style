class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        def recurse(i, n):
            if i == n - 1:
                return 0
            if i in memo:
                return memo[i]

            res = float('inf')
            for jump in range(1, nums[i]+1):
                if i + jump < n:
                    res = min(res, 1 + recurse(i + jump, n))
            memo[i] = res
            return memo[i]

        return recurse(0, n)