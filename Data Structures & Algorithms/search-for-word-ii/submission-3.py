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
        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        res = []

        def find_word(i, j, parent, path):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            c = board[i][j]
            if c not in parent.children:          # also skips visited cells marked "#"
                return

            curr = parent.children[c]
            path += c
            if curr.end_of_word:
                res.append(path)
                curr.end_of_word = False          # no duplicates

            board[i][j] = "#"                     # mark visited
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                find_word(i + di, j + dj, curr, path)
            board[i][j] = c                       # unmark

            if not curr.children and not curr.end_of_word:
                parent.children.pop(c)            # prune finished branches

        for i in range(m):
            for j in range(n):
                find_word(i, j, trie.root, "")

        return res