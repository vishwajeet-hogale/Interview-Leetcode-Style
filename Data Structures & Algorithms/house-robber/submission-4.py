class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(dp[-2]+nums[i], dp[-1]))

        return dp[-1]
        