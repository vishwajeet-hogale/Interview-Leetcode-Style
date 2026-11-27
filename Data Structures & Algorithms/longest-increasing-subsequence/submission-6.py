class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        def recurse(i, par):
            if i <= 0:
                memo[(i,par)] = 0
                return memo[(i,par)]
            if (i, par) in memo:
                return memo[(i,par)]
            if par is None:
                memo[(i,par)] = max(1 + recurse(i-1, nums[i-1]), recurse(i-1, None))
                return memo[(i,par)] 

            if nums[i-1] < par:
                memo[(i,par)] = max(1 + recurse(i-1, nums[i-1]), recurse(i-1, par))
                return memo[(i,par)]

            memo[(i,par)] = memo[(i,par)] = recurse(i-1, par)
            return memo[(i,par)]

        return recurse(n, None)

        