class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        msum = -float('inf')

        for num in nums:
            s += num
            msum = max(msum, s)
            if s < 0:
                s = 0

        return msum
        