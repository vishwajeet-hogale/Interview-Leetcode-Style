from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        vis = set(deadends)

        def get_children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res


        queue = deque([("0000", 0)])
        
        while queue:
            curr_lock_code, turns = queue.popleft()
            if curr_lock_code == target:
                return turns
            for next_lock_code in get_children(curr_lock_code):
                if next_lock_code not in vis:
                    vis.add(next_lock_code)
                    queue.append((next_lock_code, turns + 1))

        return -1
            