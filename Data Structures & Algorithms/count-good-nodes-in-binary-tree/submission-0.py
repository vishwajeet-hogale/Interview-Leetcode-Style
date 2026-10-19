# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def recurse(root, currMax):
            nonlocal cnt
            if root is None:
                return

            if currMax <= root.val:
                cnt += 1
                currMax = root.val

            recurse(root.left, currMax)
            recurse(root.right, currMax)
            return 
        
        if root is None:
            return 0

        recurse(root, root.val)
        return cnt

        