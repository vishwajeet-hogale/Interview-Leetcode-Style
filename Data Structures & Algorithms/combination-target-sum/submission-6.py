class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        vis = set()
        nums = sorted(nums)
        def recurse(target, i, temp):
            nonlocal n, res
            if i >= n:
                return
            if target == 0:
                res.append(temp)
                return 

            for j in range(i, n):
                if nums[j] > target:     # sorted, so everything after is too big
                    break
                recurse(target - nums[j], j, temp + [nums[j]])
            
            return

        recurse(target, 0, [])
        return res