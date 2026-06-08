from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def get_children(lock_state):
            options = []
            for i in range(4):
                lk_st_num = int(lock_state[i])
                choice1 = str(lock_state[:i] + str((lk_st_num - 1) % 10) + lock_state[i+1:])
                choice2 = str(lock_state[:i] + str((lk_st_num + 1) % 10) + lock_state[i+1:])
                options.extend([choice1, choice2])
            return options
        if "0000" in deadends:
            return -1
        vis = set(deadends)
        vis.add("0000")
        queue = deque([("0000", 0)])

        while queue:
            curr_state, moves = queue.popleft()
            # print(str(curr_state))
            if curr_state == target:
                return moves 
            for next_state in get_children(curr_state):
                if next_state not in vis:
                    vis.add(next_state)
                    queue.append((next_state, moves + 1))
                    

        return -1

