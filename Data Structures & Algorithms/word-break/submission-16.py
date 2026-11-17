class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        hmap = defaultdict(bool)
        def recurse(s):
            if s in hmap:
                return hmap[s]
            if s == "":
                return True 
            n = len(s)
            res = False
            for i in range(n):
                match = s[:i+1]
                if match in wordDict and recurse(s[i+1:]):
                    hmap[s] = True
                    return True 
            hmap[s] = res
            return hmap[s]

        return recurse(s)
                
        