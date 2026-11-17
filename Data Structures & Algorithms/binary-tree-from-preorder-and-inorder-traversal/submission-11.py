# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}   # value → position in inorder
        pre_i = 0                                         # next root in preorder

        def build(left, right):                           # inorder range [left, right]
            nonlocal pre_i
            if left > right:
                return None

            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            mid = idx[root_val]
            root.left = build(left, mid - 1)              # left first, matches preorder order
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
        