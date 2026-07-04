class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MyHashSet:

    def __init__(self):
        self.array = [None] * 10000

    def hash(self, key: int) -> int:
        return key % 10000

    def add(self, key: int) -> None:
        hash_location = self.hash(key)

        if self.contains(key):
            return

        node = Node(key)

        if self.array[hash_location] is None:
            self.array[hash_location] = node
            return

        curr = self.array[hash_location]
        while curr and curr.right is not None:
            curr = curr.right

        curr.right = node
        node.left = curr
        return

    def remove(self, key: int) -> None:
        hash_location = self.hash(key)

        start = self.array[hash_location]
        prev = None
        if start is None:
            return

        while start:
            if start.val == key:
                break
            prev = start
            start = start.right

        if start is None:
            return

        if prev is None:
            next_node = start.right
            if next_node:
                next_node.left = None
            self.array[hash_location] = next_node
            return

        if start.right is None:
            prev.right = None
            start.left = None
            return

        next_node = start.right
        prev.right = next_node
        next_node.left = prev
        return

    def contains(self, key: int) -> bool:
        hash_location = self.hash(key)

        curr = self.array[hash_location]

        while curr:
            if curr.val == key:
                return True
            curr = curr.right

        return False


# Your MyHashSet object will be instantiated and called