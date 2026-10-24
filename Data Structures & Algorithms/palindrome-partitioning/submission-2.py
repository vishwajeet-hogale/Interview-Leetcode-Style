class Solution:
    def __init__(self):
        self.res = []
    def check(self, s, len_s):
        l, r = 0, len_s - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def recurse(self, s, temp):
        if s == "":
            self.res.append(temp)
            return

        n = len(s)
        for i in range(n):
            lsubstr = s[:i+1]
            if self.check(lsubstr, len(lsubstr)):
                self.recurse(s[i+1:], temp + [lsubstr])

        return 


    def partition(self, s: str) -> List[List[str]]:
        self.recurse(s, [])
        return self.res



        