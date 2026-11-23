class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)

        if s % k != 0:
            return False

        s //= k                                   # CHANGE 1: integer division
        n = len(nums)
        nums.sort(reverse=True)                   # CHANGE 2: big numbers first, fails faster
        used = [False] * n                        # CHANGE 3: track which numbers are taken
        memo = dict()
        def recurse(i, target, k):                # CHANGE 4: also pass groups left
            if (i,target, k) in memo:
                return memo[(i, target, k)]
            if k == 1:                            # last group fills itself with what's left
                memo[(i, target, k)] = True
                return True
            
            if target == 0:                       # CHANGE 5: group done, start the next one
                memo[(i, target, k)] = recurse(0, s, k - 1)
                return memo[(i, target, k)]

            if i >= n:
                memo[(i, target, k)] = False
                return False

            if not used[i] and nums[i] <= target:  # CHANGE 6: skip used numbers
                used[i] = True
                if recurse(i + 1, target - nums[i], k):
                    memo[(i, target, k)] = True
                    return True
                used[i] = False                   # undo if it didn't work
            memo[(i, target, k)] = recurse(i + 1, target, k)
            return memo[(i, target, k)] 

        return recurse(0, s, k)