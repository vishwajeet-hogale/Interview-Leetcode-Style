from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        st, end, n = 0, 0, len(nums)
        res = []

        while end < n:
            # Add to monotonic queue only if it is larger than the last element in the queue
            while dq and dq[-1] < nums[end]:
                _ = dq.pop()
            dq.append(nums[end])

            # Validate the window size
            while (end - st + 1) > k:
                if dq[0] == nums[st]:
                    _ = dq.popleft()
                st += 1

            if (end - st + 1) == k:
                res.append(dq[0])

            end += 1

        return res
            
