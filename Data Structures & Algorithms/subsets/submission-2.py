from collections import defaultdict
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        vis = defaultdict(int)
        # vis[frozenset([])] = 1
        def recurse(i, temp):
            nonlocal res, n
            key = frozenset(temp)
            if i >= n:
                if key not in vis:
                    res.append(temp)
                    vis[key] = 1
                return    
            for j in range(i, n):
                recurse(j+1, temp + [nums[j]])
                recurse(j+1, temp)

        

        recurse(0, [])
        return res



        