class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res = 1
        def divide(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            res = divide(x, n // 2)
            res = res * res
            return x * res if n % 2 != 0 else res

        res = divide(x, abs(n))
        return res if n >= 0 else 1 / res
        