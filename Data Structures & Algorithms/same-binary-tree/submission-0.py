# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if root is None and sub_root is None:
                return True
            
        if (root is None and sub_root is not None) or (root is not None and sub_root is None):
            return False

        if root.val == sub_root.val:
            return True and self.isSameTree(root.left, sub_root.left) and self.isSameTree(root.right, sub_root.right)

        return False
        