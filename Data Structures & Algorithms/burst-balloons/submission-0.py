class Solution:
    memo = {}
    def maxCoins(self, nums: List[int]) -> int:

        if not nums:
            return 0

        key = tuple(nums)
        if key in self.memo:
            return self.memo[key]

        maxProfit = 0
        n = len(nums)

        for i, val in enumerate(nums):
            l = nums[i-1] if i > 0 else 1
            r = nums[i+1] if i < n - 1 else 1

            profit = l*r*val + self.maxCoins(nums[:i] + nums[i+1:])
            maxProfit = max(maxProfit, profit)

        self.memo[key] = maxProfit
        return maxProfit