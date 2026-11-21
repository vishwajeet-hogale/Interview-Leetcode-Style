class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
class MyHashMap:

    def __init__(self):
        self.map = [Node(-1, -1) for _ in range(1000)]
        
    def hash(self, key):
        return key % len(self.map)
    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]
        prev = None
        while curr != None:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.right
        
        new_node = Node(key, value)
        if curr is None: # Insert at end 
            prev.right = new_node
            new_node.left = prev
            return


        curr.right = new_node
        new_node.left = curr 


    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)]
        while curr != None:
            if curr.key == key:
                return curr.val
            curr = curr.right

        return -1

        

    def remove(self, key: int) -> None:
        prev = None
        curr = self.map[self.hash(key)]
        
        while curr != None:
            if curr.key == key:
                break
            prev = curr 
            curr = curr.right

        if curr is None:
            return
        next_node = curr.right
        if next_node is None:
            prev.right = None
        else:
            prev.right = next_node
            next_node.left = prev

        curr.left = None
        curr.right = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)