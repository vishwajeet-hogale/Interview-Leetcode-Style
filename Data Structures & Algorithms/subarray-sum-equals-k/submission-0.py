class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pr_map = defaultdict(int)
        pr_map[0] = 1
        rsum = 0
        cnt = 0
        for num in nums:
            rsum += num
            if (rsum - k) in pr_map:
                cnt += pr_map[rsum - k]
            
            pr_map[rsum] += 1

        return cnt

        
        