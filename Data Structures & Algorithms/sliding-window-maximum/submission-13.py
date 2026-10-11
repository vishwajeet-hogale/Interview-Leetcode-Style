from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        l, r, n = 0,0,len(nums)
        res = []
        while r < n:
            while window and window[-1] < nums[r]:
                _ = window.pop()
            window.append(nums[r])

            while (r - l + 1) > k:
                if window[0] == nums[l]:
                    _ = window.popleft()

                l += 1

            if (r - l + 1) == k:
                res.append(window[0])

            r += 1

        return res


            

        