class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = dict()
        def recurse(i, n):
            if i >= (n - 1):
                return True

            if i in memo:
                return memo[i]

            reached = False
            for jump in range(1, nums[i]+1):
                if recurse(i+jump, n):
                    memo[i] = True
                    return True

            memo[i] = reached
            return memo[i]
        

        return recurse(0, n)
                

         

        