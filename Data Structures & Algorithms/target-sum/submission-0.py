class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def recurse(i, target):
            if i == 0:
                if target == 0:
                    return 1
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            memo[(i,target)] = recurse(i-1, target - nums[i-1]) + recurse(i-1, target + nums[i-1])
            return memo[(i,target)]

        n = len(nums)
        return recurse(n, target)
        