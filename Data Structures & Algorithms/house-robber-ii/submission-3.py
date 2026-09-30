class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        memo1, memo2 = {}, {}
        def recurse(i):
            if i >= n - 1:
                return 0
            if i in memo1:
                return memo1[i]
            memo1[i] = max(nums[i] + recurse(i+2), recurse(i+1))
            return memo1[i]
            
        def recurse1(i):
            if i >= n:
                return 0
            if i in memo2:
                return memo2[i]
            memo2[i] =  max(nums[i] + recurse1(i+2), recurse1(i+1))
            return memo2[i]

        return max(recurse(0), recurse1(1))



            