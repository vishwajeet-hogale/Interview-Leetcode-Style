from collections import defaultdict, Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map = Counter(nums)
        n = len(nums)
        res = []
        for key in count_map:
            if count_map[key] > n // 3:
                res.append(key)

        return res
