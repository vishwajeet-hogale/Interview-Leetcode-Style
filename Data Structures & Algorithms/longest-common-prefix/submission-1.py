class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.end_of_word = True

    def find_max(self):
        curr = self.root
        prefix = ""
        while not curr.end_of_word and len(curr.children) == 1:
            # print(curr.children)
            for ch in curr.children:
                curr = curr.children[ch]
            prefix += ch

        return prefix
        


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        return trie.find_max()
    

        