class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.memo = dict()
    def build_trie(self, dictionary):
        curr = self.root
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.end_of_word = True

    def helper(self, s):

        if s == "":
            return 0
        if s in self.memo:
            return self.memo[s]
        curr = self.root
        res = 1 + self.helper(s[1:])
        for i in range(len(s)):
            c = s[i]
            if c in curr.children:
                curr = curr.children[c]
                if curr.end_of_word:
                    print(c)        
                    res = min(res, self.helper(s[i+1:]))
            else:
                break
                
                    
        self.memo[s] = res
        return self.memo[s]
            
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.build_trie(dictionary)

        return self.helper(s)
        
        

        