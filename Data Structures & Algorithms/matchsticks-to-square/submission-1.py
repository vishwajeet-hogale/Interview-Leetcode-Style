class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 4 != 0:
            return False

        s //= 4
        n = len(nums)
        nums.sort(reverse=True)
        used = [False] * n
        memo = dict()
        def recurse(i, target, k):
            key = (i, target, k, tuple(used))      # FIX: include used state in the key
            if key in memo:
                return memo[key]
            if k == 1:
                memo[key] = True
                return True

            if target == 0:
                memo[key] = recurse(0, s, k - 1)
                return memo[key]

            if i >= n:
                memo[key] = False
                return False

            if not used[i] and nums[i] <= target:
                used[i] = True
                if recurse(i + 1, target - nums[i], k):
                    memo[key] = True
                    return True
                used[i] = False

            memo[key] = recurse(i + 1, target, k)
            return memo[key]

        return recurse(0, s, 4)