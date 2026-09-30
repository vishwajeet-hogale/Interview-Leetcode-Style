class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        words = set(wordDict)
        memo = {}
        def recurse(temp_s):
            if temp_s == "":
                return True
            if temp_s in memo:
                return memo[temp_s]
            
            for i in range(len(temp_s)):
                if temp_s[:i+1] in words and recurse(temp_s[i+1:]):
                    memo[temp_s] = True
                    return memo[temp_s]


            memo[temp_s] = False 
            return memo[temp_s]



        return recurse(s)