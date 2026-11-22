class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        i, n = 0, len(nums)
        res = []
        def recurse(i, keep_idx, temp):
            if i >= n:
                if temp not in res:
                    res.append(temp)
                return

            for option in range(n):
                
                if option not in keep_idx:
                    keep_idx.add(option)
                    recurse(i+1, keep_idx, temp + [nums[option]])
                    keep_idx.remove(option)
                
        
        
        recurse(0, set(), [])
        return res

        