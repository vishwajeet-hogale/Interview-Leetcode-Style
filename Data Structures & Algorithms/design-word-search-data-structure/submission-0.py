class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        ptr = self.root

        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]

        ptr.end_of_word = True
        return

    def search(self, word: str) -> bool:
        def dfs(i, ptr):                          # FIX 1, 2: node is a parameter
            if i >= len(word):
                return ptr.end_of_word            # FIX 3
            if word[i] == ".":
                for ch in ptr.children:
                    if dfs(i+1, ptr.children[ch]):
                        return True
            else:
                if word[i] in ptr.children:
                    if dfs(i+1, ptr.children[word[i]]):
                        return True

            return False

        return dfs(0, self.root)