class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 4 != 0:
            return False

        s //= 4
        n = len(nums)
        nums.sort(reverse=True)
        if nums[0] > s:
            return False
        sides = [0] * 4

        def recurse(i):
            if i == n:                             # every stick placed
                return True

            for j in range(4):
                if sides[j] + nums[i] <= s:
                    sides[j] += nums[i]            # add stick i to side j
                    if recurse(i + 1):
                        return True
                    sides[j] -= nums[i]            # take it back out

            return False

        return recurse(0)