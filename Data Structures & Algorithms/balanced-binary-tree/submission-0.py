# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def max_depth(root):
            if root is None:
                return 0

            return 1 + max(max_depth(root.left), max_depth(root.right))

        def recurse(root):
            if root is None:
                return True

            height_l, height_r = max_depth(root.left), max_depth(root.right)
            if abs(height_r - height_l) > 1:
                return False

            return True and recurse(root.left) and recurse(root.right)

        return recurse(root)
        