# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mdiameter = 0
        def max_depth(root):
            if root is None:
                return 0

            return 1 + max(max_depth(root.left), max_depth(root.right))

        def recurse(root):
            nonlocal mdiameter
            if root is None:
                return

            mdiameter = max(mdiameter, max_depth(root.left) + max_depth(root.right))
            recurse(root.left)
            recurse(root.right)
            return

        recurse(root)
        return mdiameter


            
        