class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = dict()
        for i, c in enumerate(s):
            lastIndex[c] = i
        size = 0
        end = 0
        res = []
        print(lastIndex)
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])

            if i == end:
                res.append(size)
                size = 0

        return res
        