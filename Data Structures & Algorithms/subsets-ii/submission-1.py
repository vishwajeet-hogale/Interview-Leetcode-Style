class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        vis = set()
        n = len(nums)
        res = []
        nums = sorted(nums)
        def recurse(i, temp):

            if i >= n:
                key = "".join(str(temp))
                if key not in vis:
                    res.append(temp)
                    vis.add(key)
                return 
            for j in range(i, n):
                recurse(j+1, temp + [nums[j]])
                recurse(j+1, temp)
            return 

        recurse(0, [])
        return res
        