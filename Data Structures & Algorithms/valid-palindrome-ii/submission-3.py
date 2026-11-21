class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_pal(s1):
            l, r = 0, len(s1) - 1
            while l <= r:
                if s1[l] != s1[r]:
                    return False
                l += 1
                r -= 1

            return True

        for i in range(len(s)):
            new_str = s[:i] + s[i+1:]
            if check_pal(new_str):
                return True

        return False
        