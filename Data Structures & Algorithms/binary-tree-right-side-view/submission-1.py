# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            length = len(queue)
            temp = []
            for _ in range(length):
                node = queue.popleft()
                if node is None:
                    continue

                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if temp:
                res.append(temp[-1])

        return res
        