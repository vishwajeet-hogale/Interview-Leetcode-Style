class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1,1 
        res = max(nums)
        for n in nums:
            if n == 0:
                currMax, currMin = 1,1
                continue

            temp = n * currMax
            currMax = max(n*currMax, max(n * currMin, n))
            currMin = min(temp, min(n*currMin, n))
            res = max(currMax, res)

        return res
            


        