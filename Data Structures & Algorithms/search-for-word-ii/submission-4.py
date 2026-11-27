class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        vis = set()
        trie_root = trie.root
        m, n = len(board), len(board[0])

        def find_word(i, j, curr, path):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in vis or board[i][j] not in curr.children:
                return False

            curr = curr.children[board[i][j]]
            path += board[i][j]
            found = False
            if curr.end_of_word:
                res.append(path)
                curr.end_of_word = False
                found = True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            vis.add((i, j))
            for di, dj in directions:
                if find_word(i + di, j + dj, curr, path):
                    found = True
            vis.remove((i, j))

            return found

        for i in range(m):
            for j in range(n):
                find_word(i, j, trie_root, "")

        return res