from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        i, n = 0, len(path)
        path = path.split("/")
        print(path)
        for p in path:
            if p == "..":
                if stack:
                    _ = stack.pop()
                continue
            elif p == "." or p == "":
                continue
            stack.append(p)
        print(stack)
        return "/" + "/".join(stack)