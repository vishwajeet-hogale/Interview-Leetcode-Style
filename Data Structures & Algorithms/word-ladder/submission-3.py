from collections import deque
class Solution:
    def find_neighbors(self, curr, words):
        options = []
        for i in range(len(curr)):
            key = curr[:i] + "*" + curr[i+1:]
            for word in words:
                match_key = word[:i] + "*" + word[i+1:]
                if key == match_key:
                    options.append(word)
        return options
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        vis = set()
        queue = deque([(beginWord, 0)])
        vis.add(beginWord)
        while queue:
            curr_word, jumps = queue.popleft()
            if curr_word == endWord:
                return jumps + 1
            for next_word in self.find_neighbors(curr_word, wordList):
                if next_word not in vis:
                    vis.add(next_word)
                    queue.append((next_word, jumps+1))

        return 0
        