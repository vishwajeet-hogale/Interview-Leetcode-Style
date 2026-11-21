class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = dict()

        hmap[0] = 1
        s = 0
        cnt = 0
        for num in nums:
            s += num

            if (s - k) in hmap:
                cnt += hmap[s-k]

            hmap[s] = hmap.get(s,0) + 1

        return cnt
                

        