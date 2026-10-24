class Solution:
    def __init__(self):
        self.phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.res = []
    def recurse(self, i, temp, n, digits):
        if i >= n:
            self.res.append(temp)
            return

        for letter in self.phone_map[digits[i]]:
            self.recurse(i+1, temp + letter, n, digits)


    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return self.res
        self.recurse(0, "", len(digits), digits)
        return self.res


        