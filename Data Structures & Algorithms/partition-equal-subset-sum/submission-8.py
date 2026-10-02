class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = total // 2
        dp = [[False for _ in range(total + 1)] for _ in range(len(nums)+1)]
        m, n = len(nums)+1, total + 1
        for i in range(m):
            dp[i][0] = False

        for j in range(total + 1):
            dp[0][j] = False

        dp[0][0] = True

        for i in range(1,m):
            for j in range(1,n):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m-1][n-1]