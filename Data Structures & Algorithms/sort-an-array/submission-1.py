class Solution:
    def merge(self, a, b):
            res = []
            i, j = 0, 0
            m, n = len(a), len(b)
            while i < m and j < n:
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                elif a[i] > b[j]:
                    res.append(b[j])
                    j += 1
                else:
                    res.extend([a[i], b[j]])
                    i += 1
                    j += 1


            while i < m:
                res.append(a[i])
                i += 1

            while j < n:
                res.append(b[j])
                j += 1

            return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums)
        m = m // 2
        l = self.sortArray(nums[:m])
        r = self.sortArray(nums[m:])

        return self.merge(l,r)
        


        
        