class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0]*n
        r = [0]*n

        for i in range(1,n):
            l[i] = max(l[i-1], height[i-1])

        for i in range(n-2,0,-1):
            r[i] = max(r[i+1], height[i+1])

        total = 0

        for i in range(n):
            total += max(min(l[i], r[i]) - height[i], 0)

        return total

        