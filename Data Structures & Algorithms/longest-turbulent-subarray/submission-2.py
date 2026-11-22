class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        signs = []
        n = len(arr)
        # if n == 0:
        #     return 1
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                signs.append(1)
            elif arr[i-1] > arr[i]:
                signs.append(-1)
            else:
                signs.append(0)

        if len(signs) == 0:
            return 1
        best = 0
        prev = 0
        cnt = 1
        for i in signs:
            if i == 0:
                cnt = 1
            elif i == -prev:
                cnt += 1
            else:
                cnt = 2
            prev = i
            best = max(best, cnt)


        return best 

        
        
   

        