# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def recurse(root):
            nonlocal res
            nonlocal k
            if root is None:
                return 

            recurse(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return

            recurse(root.right)

        recurse(root)
        return res

        