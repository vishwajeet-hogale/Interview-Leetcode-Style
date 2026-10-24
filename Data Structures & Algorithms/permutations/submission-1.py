class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        picked = []
        res = []
        def recurse(temp, picked):
            nonlocal res
            if len(picked) >= n:
                res.append(temp)
                return

            
            for choice in range(n):
                if choice in picked:
                    continue 
                recurse(temp + [nums[choice]], picked + [choice])

            return 

        recurse([],[])
        return res



        