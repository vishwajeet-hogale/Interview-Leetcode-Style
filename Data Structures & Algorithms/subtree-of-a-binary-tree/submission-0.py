# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        def check_tree(root, sub_root):
            if root is None and sub_root is None:
                return True
            
            if (root is None and sub_root is not None) or (root is not None and sub_root is None):
                return False

            if root.val == sub_root.val:
                return True and check_tree(root.left, sub_root.left) and check_tree(root.right, sub_root.right)

            return False

        found = False
        def recurse(root):
            nonlocal found
            if root is None:
                return

            found = found or check_tree(root, sub_root)

            recurse(root.left)
            recurse(root.right)

            return 


        recurse(root)
        return found

            
        