from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)              # FIX 3: list per key

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))  # FIX 3: append, stays sorted

    def search(self, time_values: list[tuple], timestamp: int):
        l, r = 0, len(time_values) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if time_values[m][0] > timestamp:
                r = m - 1
            else:
                l = m
        return l

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map:
            all_values = self.hash_map[key]            # FIX 3: no copy
            sidx = self.search(all_values, timestamp)
            if all_values[sidx][0] <= timestamp:
                return all_values[sidx][1]
        return ""